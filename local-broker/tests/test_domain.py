"""Pruebas del dominio de agencias, tenants y expedientes (Spec 001, T2)."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from broker_core.domain import (  # noqa: E402
    CaseState,
    TenantIsolationError,
    create_case,
    create_demo_agency,
    get_case,
    transition_case,
)


class DomainTests(unittest.TestCase):
    def setUp(self) -> None:
        self.agency = create_demo_agency()

    def test_demo_agency_has_stable_identity(self) -> None:
        self.assertEqual(self.agency.display_name, "Inmobiliaria Demo Broker")
        self.assertEqual(self.agency.tenant_id, "tenant-inmobiliaria-demo-broker")
        self.assertEqual(self.agency.agency_slug, "inmobiliaria-demo-broker")

    def test_case_belongs_to_agency_and_starts_in_intake(self) -> None:
        case = create_case(self.agency, "Validar una captación sintética en Lima")

        self.assertEqual(case.tenant_id, self.agency.tenant_id)
        self.assertEqual(case.agency_slug, self.agency.agency_slug)
        self.assertEqual(case.state, CaseState.INTAKE)
        self.assertTrue(case.case_id.startswith("case-"))

    def test_case_transitions_follow_the_declared_flow(self) -> None:
        case = create_case(self.agency, "Revisar un lead sintético")

        for state in (
            CaseState.TRIAGED,
            CaseState.IN_PROGRESS,
            CaseState.QUALITY_REVIEW,
        ):
            case = transition_case(case, state)

        self.assertEqual(case.state, CaseState.QUALITY_REVIEW)

    def test_case_cannot_skip_quality_review_before_closing(self) -> None:
        case = create_case(self.agency, "Cerrar expediente de prueba")

        with self.assertRaises(ValueError):
            transition_case(case, CaseState.CLOSED)

    def test_case_lookup_rejects_a_different_tenant(self) -> None:
        case = create_case(self.agency, "Comprobar aislamiento")
        other_agency = create_demo_agency(
            display_name="Otra Agencia Sintética",
            tenant_id="tenant-otra-agencia",
            agency_slug="otra-agencia",
        )

        with self.assertRaises(TenantIsolationError):
            get_case(case, other_agency.tenant_id)


if __name__ == "__main__":
    unittest.main()
