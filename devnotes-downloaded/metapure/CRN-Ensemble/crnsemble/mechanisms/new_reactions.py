from biocrnpyler import Reaction
from biocrnpyler.mechanisms import MichaelisMentenReversible


def reversed_binding_rxn2(product, enzyme, complex2, kb2, ku2):
    """
    New version of binding_rxn2 with reversed direction:
    complex2 <-> product + enzyme
    """
    return Reaction.from_massaction(
        inputs=[complex2],
        outputs=[product, enzyme],
        k_forward=ku2,
        k_reverse=kb2,
    )


class MichaelisMentenReversibleMod(MichaelisMentenReversible):
    """
    Subclass of MichaelisMentenReversible where only the second binding reaction
    direction is changed.
    """

    def update_reactions(
        self,
        Enzyme,
        Sub,
        Prod,
        component=None,
        part_id=None,
        complex=None,
        complex2=None,
        kb=None,
        ku=None,
        kcat=None,
        **keywords,
    ):
        # Let the parent class resolve/get parameters (or use explicit ones).
        rxns = super().update_reactions(
            Enzyme=Enzyme,
            Sub=Sub,
            Prod=Prod,
            component=component,
            part_id=part_id,
            complex=complex,
            complex2=complex2,
            kb=kb,
            ku=ku,
            kcat=kcat,
            **keywords,
        )

        # Replace only the second binding reaction with reversed direction.
        # Reuse the parent reaction's underlying parameter objects so the
        # propensity structure (e.g., _k_forward._value) is preserved.
        rxn2 = rxns[1]
        complex2_species = rxn2.outputs[0].species
        kb2 = rxn2._propensity_type._k_forward
        ku2 = rxn2._propensity_type._k_reverse
        rxns[1] = reversed_binding_rxn2(
            product=Prod,
            enzyme=Enzyme,
            complex2=complex2_species,
            kb2=kb2,
            ku2=ku2,
        )
        return rxns
