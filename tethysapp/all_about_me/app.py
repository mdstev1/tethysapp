from tethys_sdk.base import TethysAppBase, url_map_maker


class AllAboutMe(TethysAppBase):
    """
    Tethys app class for All About Me.
    """

    name = 'All About Me'
    index = 'all_about_me:home'
    icon = 'all_about_me/images/Michael.png'
    package = 'all_about_me'
    root_url = 'all-about-me'
    color = '#5F9EA0'
    description = 'This app provides a brief description of the author.'
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
                url='all-about-me',
                controller='all_about_me.controllers.home'
            ),
            UrlMap(
                name='map',
                url='all-about-me/map',
                controller='all_about_me.controllers.map'
            ),
        )

        return url_maps
