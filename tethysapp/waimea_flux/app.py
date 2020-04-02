from tethys_sdk.base import TethysAppBase, url_map_maker


class WaimeaFlux(TethysAppBase):
    """
    Tethys app class for Waimea Flux.
    """

    name = 'Waimea Data'
    index = 'waimea_flux:home'
    icon = 'waimea_flux/images/icon.gif'
    package = 'waimea_flux'
    root_url = 'waimea-flux'
    color = '#8e44ad'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='waimea-flux',
                controller='waimea_flux.controllers.home'
            ),
            UrlMap(
                name='About',
                url='About',
                controller='waimea_flux.controllers.About'
            ),
            UrlMap(
                name='Data',
                url='Data',
                controller='waimea_flux.controllers.Data'
            ),
            UrlMap(
                name='New_Data',
                url='New_Data',
                controller='waimea_flux.controllers.New_Data'
            )
        )

        return url_maps
