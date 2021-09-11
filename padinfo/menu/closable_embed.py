from discordmenu.embed.control import EmbedControl
from discordmenu.embed.menu import EmbedMenu

from tsutils.menu.panes import MenuPanes
from padinfo.view.awakening_help import AwakeningHelpView
from padinfo.view.closable_embed import ClosableEmbedViewState
from padinfo.view.experience_curve import ExperienceCurveView
from padinfo.view.id_traceback import IdTracebackView

view_types = {
    AwakeningHelpView.VIEW_TYPE: AwakeningHelpView,
    IdTracebackView.VIEW_TYPE: IdTracebackView,
    ExperienceCurveView.VIEW_TYPE: ExperienceCurveView,
}


class ClosableEmbedMenu:
    MENU_TYPE = 'ClosableEmbedMenu'
    message = None

    @staticmethod
    def menu():
        embed = EmbedMenu({}, ClosableEmbedMenu.message_control)
        return embed

    @staticmethod
    def message_control(state: ClosableEmbedViewState):
        view = view_types[state.view_type]
        return EmbedControl(
            [view.embed(state, state.props)],
            []
        )


class ClosableEmbedMenuPanes(MenuPanes):
    pass
