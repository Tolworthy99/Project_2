from tethys_sdk.base import TethysAppBase, url_map_maker


class WaimeaFlux(TethysAppBase):
    """
    Tethys app class for Waimea Flux.
    """

    name = 'Kauai Water Data'
    index = 'waimea_flux:home'
    icon = 'waimea_flux/images/Waimea_Canyon.jpeg'
    package = 'waimea_flux'
    root_url = 'waimea-flux'
    color = '#8e44ad'
    description = 'An app holding water and soil data for the island of Kauai, Hawaii, US'
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
                name='Geolmap',
                url='Geolmap',
                controller='waimea_flux.controllers.Geolmap'
            ),
            UrlMap(
                name='Othermap',
                url='Othermap',
                controller='waimea_flux.controllers.Othermap'
            ),
            UrlMap(
                name='New_Data',
                url='New_Data',
                controller='waimea_flux.controllers.New_Data'
            ),
            UrlMap(
                name='Datamap',
                url='Datamap',
                controller='waimea_flux.controllers.Datamap'
            )
        )

        return url_maps
