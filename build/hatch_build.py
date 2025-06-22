import os

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        """This method is called before the build process starts."""
        # What happens if we're not using a wheel ?
        if self.target_name != "wheel":
            return

        target_arch = os.environ.get("CIBW_ARCHS", None)
        target_os_info = os.environ.get("CIBW_PLATFORM", None)

        assert target_arch is not None, f"CIBW_ARCHS not set see: {BUILD_TARGET}"
        assert target_os_info is not None, f"CIBW_PLATFORM not set see: {BUILD_TARGET}"

        # # Access the project metadata
        # metadata = self.root.metadata
        #
        # # Access the extras defined in the project
        # extras = metadata.get("optional-dependencies", {})
        #
        # # Get current include patterns from build data
        # include_patterns = build_data.get("include", [])
        #
        # # Check if specific extras are requested and modify included files
        # if "cli" in extras:
        #     print("CLI extra detected, including executable files")
        #     # Add the CLI executable file pattern to includes
        #     include_patterns.append("src/*/cli_executable*")
        #
        # # Update the build data with modified include patterns
        # build_data["include"] = include_patterns

    def finalize(self, version, build_data, artifact_path):
        """This method is called after the build process completes.
        You could also use this to modify the final artifact if needed.
        """
