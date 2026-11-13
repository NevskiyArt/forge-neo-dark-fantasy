"""Optional visual theme for Forge NEO. No model or generation changes."""
import gradio as gr
from modules import script_callbacks, shared
from modules.options import OptionInfo


def register_settings():
    shared.opts.add_option(
        "forge_neo_fantasy_theme",
        OptionInfo(
            "Стандартная",
            "Оформление FORGE NEO",
            gr.Radio,
            {"choices": ["Стандартная", "Dark Fantasy"]},
            section=("forge_neo_dark_fantasy", "FORGE NEO — тема"),
        ).info("Выберите оформление и нажмите Apply settings / Применить настройки. Перезапуск не нужен."),
    )


script_callbacks.on_ui_settings(register_settings)
