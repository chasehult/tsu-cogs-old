from typing import List

from discordmenu.embed.components import EmbedMain
from discordmenu.embed.view import EmbedView

from padinfo.common.config import UserConfig
from padinfo.view.components.base import pad_info_footer_with_state
from padinfo.view.components.view_state_base import ViewStateBase

class SimpleViewState(ViewStateBase):
    def __init__(self, original_author_id, menu_type, raw_query,
                 color, message, message2,
                 reaction_list: List[str] = None):
        super().__init__(original_author_id, menu_type, raw_query, reaction_list=reaction_list)
        self.message = message
        self.message2 = message2
        self.color = color

    def serialize(self):
        ret = super().serialize()
        ret.update({
            'message': self.message,
            'message2': self.message2
        })
        return ret

    @classmethod
    async def deserialize(cls, dgcog, user_config: UserConfig, ims: dict):
        original_author_id = ims['original_author_id']
        menu_type = ims['menu_type']
        raw_query = ims.get('raw_query')
        return cls(original_author_id, menu_type, raw_query, user_config.color, ims.get('message'),
                   reaction_list=ims.get('reaction_list'))


class SimpleTextView:
    VIEW_TYPE = 'SimpleText'

    @staticmethod
    def embed(state: SimpleViewState):
        return EmbedView(
            EmbedMain(
                color=state.color,
                description=state.message
            ),
            embed_footer=pad_info_footer_with_state(state),
        )
