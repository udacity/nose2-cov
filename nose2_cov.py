"""Coverage plugin for nose2."""

import nose2
import sys


class CovPlugin(nose2.events.Plugin):

    configSection = 'cov'
    commandLineSwitch = ('C', 'with-cov', 'Turn on coverage collection')

    def __init__(self):
        """Get our config and add our options."""

        self.conSource = self.config.as_list('cov', [])
        self.conReport = self.config.as_list('cov-report', [])
        self.conConfig = self.config.as_str('cov-config', '').strip()

        group = self.session.pluginargs
        group.add_argument('--cov', action='append', default=[], metavar='path',
                           dest='cov_source',
                           help='measure coverage for filesystem path (multi-allowed)')
        group.add_argument('--cov-report', action='append', default=[], metavar='type',
                           choices=['term', 'term-missing', 'annotate', 'html', 'xml'],
                           dest='cov_report',
                           help='type of report to generate: term, term-missing, annotate, html, xml (multi-allowed)')
        group.add_argument('--cov-config', action='store', default='', metavar='path',
                           dest='cov_config',
                           help='config file for coverage, default: .coveragerc')

    def handleArgs(self, event):
        """Get our options in order command line, config file, hard coded."""

        self.covSource = event.args.cov_source or self.conSource
        self.covReport = event.args.cov_report or self.conReport or ['term']
        self.covConfig = event.args.cov_config or self.conConfig or '.coveragerc'

    def startTestRun(self, event):
        """If we are enabled then start coverage."""

        if self.covSource:
            import cov_core
            self.covController = cov_core.Central(self.covSource, self.covReport, self.covConfig)
            self.covController.start()

    def stopTestRun(self, event):
        """If we are enabled then produce coverage reports."""

        if self.covSource:
            stream = nose2.util._WritelnDecorator(sys.stderr)
            self.covController.finish()
            self.covController.summary(stream)
