import logging
import logging.config
config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(levelname)s "%(pathname)s:%(lineno)s":%(funcName)s() - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'better_log.handler.ColorHandler',
            'formatter': 'default',
        },
        # 'file_info': {
        #     'class': 'logging.handlers.TimedRotatingFileHandler',
        #     'level': 'INFO',
        #     'formatter': 'default',
        #     'filename': os.path.join(log_dir, "service_info.log"),
        #     "when": 'midnight',
        #     "backupCount": 10,
        #     "encoding": "utf8"
        # },
    },
    'root': {
        'handlers': ['console'],
        'level': "INFO"
    }
}
logging.config.dictConfig(config)
