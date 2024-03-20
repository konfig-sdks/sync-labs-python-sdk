operation_parameter_map = {
    '/animate-POST': {
        'parameters': [
            {
                'name': 'videoUrl'
            },
            {
                'name': 'transcript'
            },
            {
                'name': 'voiceId'
            },
            {
                'name': 'model'
            },
            {
                'name': 'maxCredits'
            },
            {
                'name': 'webhookUrl'
            },
        ]
    },
    '/animate/cost-GET': {
        'parameters': [
            {
                'name': 'transcript'
            },
            {
                'name': 'transcriptUrl'
            },
        ]
    },
    '/animate/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/lipsync/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/lipsync-POST': {
        'parameters': [
            {
                'name': 'audioUrl'
            },
            {
                'name': 'videoUrl'
            },
            {
                'name': 'synergize'
            },
            {
                'name': 'maxCredits'
            },
            {
                'name': 'webhookUrl'
            },
            {
                'name': 'model'
            },
        ]
    },
    '/lipsync/cost-GET': {
        'parameters': [
            {
                'name': 'audioUrl'
            },
            {
                'name': 'videoUrl'
            },
        ]
    },
    '/speak/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/speak-POST': {
        'parameters': [
            {
                'name': 'transcript'
            },
            {
                'name': 'voiceId'
            },
            {
                'name': 'maxCredits'
            },
            {
                'name': 'webhookUrl'
            },
        ]
    },
    '/speak/cost-GET': {
        'parameters': [
            {
                'name': 'transcript'
            },
            {
                'name': 'transcriptUrl'
            },
        ]
    },
    '/translate/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/translate-POST': {
        'parameters': [
            {
                'name': 'videoUrl'
            },
            {
                'name': 'targetLanguage'
            },
            {
                'name': 'maxCredits'
            },
            {
                'name': 'webhookUrl'
            },
            {
                'name': 'model'
            },
        ]
    },
    '/translate/cost-GET': {
        'parameters': [
            {
                'name': 'videoUrl'
            },
        ]
    },
    '/video/cost-GET': {
        'parameters': [
            {
                'name': 'audioUrl'
            },
            {
                'name': 'videoUrl'
            },
        ]
    },
    '/video/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/video-POST': {
        'parameters': [
            {
                'name': 'audioUrl'
            },
            {
                'name': 'videoUrl'
            },
            {
                'name': 'synergize'
            },
            {
                'name': 'maxCredits'
            },
            {
                'name': 'webhookUrl'
            },
            {
                'name': 'model'
            },
        ]
    },
    '/voices-GET': {
        'parameters': [
        ]
    },
};