"""
* MDFC TEMPLATES
"""
# Standard Library
from functools import cached_property
from typing import Optional, Callable

# Third Party Imports
from photoshop.api._artlayer import ArtLayer

# Local Imports
from src.enums.layers import LAYERS
import src.helpers as psd
from src.templates._core import BaseTemplate, NormalTemplate
from src.templates._vector import VectorTemplate
from src.text_layers import ScaledTextField, FormattedTextField

"""
* Modifier Classes
"""


class MDFCMod(BaseTemplate):
    """
    * Modifier for MDFC templates.

    Adds:
        * MDFC Left text layer (opposing side type)
        * MDFC Right text layer (opposing side cost or land tap ability)
        * Top (arrow icon) and bottom (opposing side info) MDFC layer elements
    """

    """
    * Mixin Methods
    """

    @cached_property
    def frame_layer_methods(self) -> list[Callable]:
        """Add MDFC frame layers step."""
        parent_funcs = super().frame_layer_methods
        return [*parent_funcs, self.enable_mdfc_layers] if self.is_mdfc else parent_funcs

    @cached_property
    def text_layer_methods(self) -> list[Callable]:
        """Add MDFC text layers step."""
        parent_funcs = super().text_layer_methods
        return [*parent_funcs, self.text_layers_mdfc] if self.is_mdfc else parent_funcs

    """
    * MDFC Colors
    """

    @cached_property
    def mdfc_icon_color(self) -> str:
        """Layer name for the MDFC top icon color."""
        if self.twins == LAYERS.LAND:
            return LAYERS.COLORLESS
        return self.twins

    @cached_property
    def mdfc_bar_color(self) -> str:
        """Layer name for the MDFC top icon color."""
        if self.layout.other_face_twins == LAYERS.LAND:
            return LAYERS.COLORLESS
        return self.layout.other_face_twins

    """
    * MDFC Text Layers
    """

    @cached_property
    def text_layer_mdfc_left(self) -> Optional[ArtLayer]:
        """The back face card type."""
        return psd.getLayer(LAYERS.LEFT, self.dfc_group)

    @cached_property
    def text_layer_mdfc_right(self) -> Optional[ArtLayer]:
        """The back face mana cost or land tap ability."""
        return psd.getLayer(LAYERS.RIGHT, self.dfc_group)

    """
    * MDFC Frame Layer Methods
    """

    def enable_mdfc_layers(self) -> None:
        """Enable layers that are required by modal double faced cards."""

        # MDFC elements at the top and bottom of the card
        psd.getLayer(self.mdfc_icon_color, [self.dfc_group, LAYERS.TOP]).visible = True
        psd.getLayer(self.mdfc_bar_color, [self.dfc_group, LAYERS.BOTTOM]).visible = True

        # Front and back side layers
        if self.is_front:
            return self.enable_mdfc_layers_front()
        return self.enable_mdfc_layers_back()

    def enable_mdfc_layers_front(self) -> None:
        """Enable front side MDFC layers."""
        pass

    def enable_mdfc_layers_back(self) -> None:
        """Enable back side MDFC layers."""
        pass

    """
    * MDFC Text Layer Methods
    """

    def text_layers_mdfc(self) -> None:
        """Adds and modifies text layers required by modal double faced cards."""

        # Add mdfc text layers
        self.text.extend([
            FormattedTextField(
                layer=self.text_layer_mdfc_right,
                contents=self.layout.other_face_right),
            ScaledTextField(
                layer=self.text_layer_mdfc_left,
                contents=self.layout.other_face_left,
                reference=self.text_layer_mdfc_right)])

        # Front and back side layers
        if self.is_front:
            return self.text_layers_mdfc_front()
        return self.text_layers_mdfc_back()

    def text_layers_mdfc_front(self) -> None:
        """Add or modify front side MDFC tex layers."""
        pass

    def text_layers_mdfc_back(self) -> None:
        """Add or modify back side MDFC text layers."""
        pass


class VectorMDFCMod(MDFCMod, VectorTemplate):
    """MDFC mod for vector templates."""

    """
    * MDFC Frame Layer Methods
    """

    def enable_mdfc_layers(self) -> None:
        """Enable group containing MDFC layers."""
        self.dfc_group.visible = True
        super().enable_mdfc_layers()


"""
* Template Classes
"""


class MDFCTemplate(MDFCMod, NormalTemplate):
    """Raster template for Modal Double Faced cards introduced in Zendikar Rising."""
