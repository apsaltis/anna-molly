"""
Poll Script for Tukeys Outlier Filter
"""
import sys
sys.path.append('../')

from .. import app
from tukeys_filter import TukeysFilter
from lib.modules.base_task import BaseTask
from lib.modules import config as config_loader


class PollTukeysFilter(BaseTask):

    def __init__(self, config, logger, options):
        super(PollTukeysFilter, self).__init__(config, logger, resource={'metric_sink': 'RedisSink'})
        self.plugin = 'TukeysFilter'

    def run(self):
        """
        """
        try:
            algo_config = config_loader.load('/opt/anna-molly/config/services.json')
            algo_config = algo_config.get(self.plugin)
        except AttributeError:
            return None
        for service, options in algo_config.iteritems():
            if service and options:
                params = {'params': options, 'service': service}
                app.task_runner.delay(TukeysFilter, params)
        return True
