"""Template loading and rendering utilities."""

from pathlib import Path

from jinja2 import Environment, FileSystemLoader


class TemplateRenderer:
    """Handle template loading and rendering."""

    def __init__(self):
        """Initialize the template renderer with the assets directory."""
        self._assets_dir = Path(__file__).parent / "assets"
        self._env = Environment(loader=FileSystemLoader(self._assets_dir))

        # Pre-load templates
        self._config_template = self._env.get_template("template_config.yaml")
        self._system_prompt_template = self._env.get_template("system_prompt.md")
        self._user_prompt_template = self._env.get_template("user_prompt.md")

    @property
    def assets_dir(self) -> Path:
        """Get the assets directory path."""
        return self._assets_dir

    def render_system_prompt(self) -> str:
        """Render the system prompt template."""
        return self._system_prompt_template.render()

    def render_user_prompt(self, status: str, diff: str, use_emojis: bool = False) -> str:
        """Render the user prompt template with git status and diff.

        Args:
            status: Output of git status command
            diff: Output of git diff command
            use_emojis: Whether to enable emoji support

        Returns:
            Rendered user prompt template
        """
        return self._user_prompt_template.render(status=status, diff=diff, use_emojis=use_emojis)

    def render_config_template(self) -> str:
        """Render the configuration template.

        Returns:
            Rendered configuration template
        """
        return self._config_template.render()


renderer = TemplateRenderer()
