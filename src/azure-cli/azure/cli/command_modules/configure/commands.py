# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    configure_custom = CliCommandType(operations_tmpl='azure.cli.command_modules.configure.custom#{}')

    with self.command_group('', configure_custom) as g:
        g.command('configure', 'handle_configure')

    with self.command_group('cache', configure_custom, is_preview=True) as g:
        g.command('list', 'list_cache_contents')
        g.command('show', 'show_cache_contents')
        g.command('delete', 'delete_cache_contents')
        g.command('purge', 'purge_cache_contents')

    with self.command_group('local-context', configure_custom, is_experimental=True) as g:
        g.command('on', 'turn_local_context_on')
        g.command('off', 'turn_local_context_off')
