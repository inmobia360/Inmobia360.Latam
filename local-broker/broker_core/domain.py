"""Entidades y transiciones mínimas del expediente inmobiliario."""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import StrEnum
from uuid import uuid4


class CaseState(StrEnum):
    INTAKE = "intake"
    TRIAGED = "triaged"
    IN_PROGRESS = "in_progress"
    QUALITY_REVIEW = "quality_review"
    APPROVED = "approved"
    CLOSED = "closed"
    WAITING_USER = "waiting_user"
    BLOCKED = "blocked"
    CANCELLED = "cancelled"
    REOPENED = "reopened"


class TenantIsolationError(ValueError):
    """Indica que se intentó leer un expediente desde otro tenant."""


@dataclass(frozen=True)
class Agency:
    display_name: str
    tenant_id: str
    agency_slug: str


@dataclass(frozen=True)
class Case:
    case_id: str
    tenant_id: str
    agency_slug: str
    objective: str
    state: CaseState = CaseState.INTAKE


def create_demo_agency(
    display_name: str = "Inmobiliaria Demo Broker",
    tenant_id: str = "tenant-inmobiliaria-demo-broker",
    agency_slug: str = "inmobiliaria-demo-broker",
) -> Agency:
    """Crea la identidad sintética usada por las pruebas locales."""
    if not display_name.strip() or not tenant_id.strip() or not agency_slug.strip():
        raise ValueError("La agencia debe tener nombre, tenant y slug no vacíos.")
    return Agency(display_name, tenant_id, agency_slug)


def create_case(agency: Agency, objective: str) -> Case:
    """Crea un expediente asociado a una única agencia."""
    if not objective.strip():
        raise ValueError("El objetivo del expediente no puede estar vacío.")
    return Case(
        case_id=f"case-{uuid4().hex}",
        tenant_id=agency.tenant_id,
        agency_slug=agency.agency_slug,
        objective=objective.strip(),
    )


_ALLOWED_TRANSITIONS: dict[CaseState, frozenset[CaseState]] = {
    CaseState.INTAKE: frozenset({CaseState.TRIAGED, CaseState.WAITING_USER, CaseState.BLOCKED}),
    CaseState.TRIAGED: frozenset({CaseState.IN_PROGRESS, CaseState.WAITING_USER, CaseState.BLOCKED}),
    CaseState.IN_PROGRESS: frozenset({CaseState.QUALITY_REVIEW, CaseState.WAITING_USER, CaseState.BLOCKED}),
    CaseState.QUALITY_REVIEW: frozenset({CaseState.APPROVED, CaseState.IN_PROGRESS, CaseState.BLOCKED}),
    CaseState.APPROVED: frozenset({CaseState.CLOSED, CaseState.REOPENED}),
    CaseState.CLOSED: frozenset({CaseState.REOPENED}),
    CaseState.WAITING_USER: frozenset({CaseState.IN_PROGRESS, CaseState.CANCELLED}),
    CaseState.BLOCKED: frozenset({CaseState.IN_PROGRESS, CaseState.CANCELLED}),
    CaseState.CANCELLED: frozenset({CaseState.REOPENED}),
    CaseState.REOPENED: frozenset({CaseState.IN_PROGRESS, CaseState.CANCELLED}),
}


def transition_case(case: Case, target: CaseState) -> Case:
    """Aplica una transición explícita del ciclo de vida del expediente."""
    if target not in _ALLOWED_TRANSITIONS[case.state]:
        raise ValueError(f"Transición no permitida: {case.state} -> {target}.")
    return replace(case, state=target)


def get_case(case: Case, tenant_id: str) -> Case:
    """Devuelve el expediente solo si pertenece al tenant solicitado."""
    if case.tenant_id != tenant_id:
        raise TenantIsolationError("El expediente pertenece a otro tenant.")
    return case
