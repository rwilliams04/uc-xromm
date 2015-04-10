config = {

    # prompts to present when creating a new study
    'study': [
        [
            'name',                 # key name for json output
            'Name of study?',       # prompt
            '''
            Your study name should only consist of alphanumeric characters.  
            Example: "Pig Chewing Experiment".
            ''',                    # extra usage/help/info/examples
            [],                     # enumerated options (or null list if none)
            r'\w{3}'                # regex for sanity check on input
        ],
        [
            'desc',    
            'Description of study?', 
            '''
            Please provide a short description of the purpose and aim of 
            this study.
            ''',                    # extra usage/help/info/examples
            [], 
            r'\w{3}'
        ],
        [
            'pi',      
            'Name of Principal Investigator?', 
            '',                     # extra usage/help/info/examples
            ['Callum Ross'],        # enumerated option
            r'^\d$'                 # input must be numeric w/ enum options
        ],
        [
            'leader',  
            'Name of study leader?', 
            '''
            The lab member most responsible for conducting this
            study.
            ''',                    # extra usage/help/info/examples
            ['Callum Ross', 'Kazutaka Takashi'], 
            r'^\d$'
        ],
        [
            'meta_public',  
            'Metadata for this study is public? (y|n)',
            '''
            Can the metadata for this study be made publicly available?
            Use `y` for yes or `n` for no.
            ''',
            ['y', 'n'], 
            r'^[yn]$'
        ],
        [
            'data_public',  
            'Data for this study is public? (y|n)',
            '''
            Can the data files for this study be made publicly available?
            Use `y` for yes or `n` for no.
            ''',
            ['y', 'n'], 
            r'^[yn]$'
        ],
        [
            'notes',  
            'Additional notes or comments? (hit return for none)',
            '''
            Here you can provide additional info pertaining to this study
            that might be useful for future reference.
            ''',
            [],
            r'\w?'
        ]
    ],

    # prompt to present when creating a new trial
    'trial': [
        [
            'type',  
            'Type of trial?',
            '''
            "Calibration" trials are ...

            ''',
            ['regular', 'calibration'],
            r'^[1-2]$'
        ]
    ],

    # prompts to present when creating a regular trial
    'regular_trial': [
        [
            'name',
            'Trial name? (max 50 chars)', 
            "Name of this trial?",          # extra usage/examples/info
            [],
            r'\w[a-z_ ]+'
        ],
        [
            'date',
            "Trial date? (YYYY/MM/DD)", 
            "Date of this trial?",          # extra usage/examples/info
            [],
            r'^20\d{2}/\d{2}/\d{2}'
        ]
    ],

    # prompts to present when creating a calibration trial
    'calibration_trial': [
        [
            'name',
            'Trial name? (max 50 chars)', 
            "Name of this trial?",          # extra usage/examples/info
            [],
            r'\w[a-z_ ]+'
        ],
        [
            'date',
            "Trial date? (YYYY/MM/DD)", 
            "Date of this trial?",          # extra usage/examples/info
            [],
            r'^20\d{2}/\d{2}/\d{2}'
        ]
    ],

    # prompts to present when transferring a data file
    'file_transfer': [
        [
            'filetype',
            "Type of file?",
            "Please choose one of the enumerated options.",
            [
                ("X-Ray Video", 'file_xray_vid'),
                ("Undistortion Grid", 'file_u_grid'),
                ("Calibration Object", 'file_calib')
                # ... &c.
            ],
            r'^\d$'
        ]
    ],

    # prompts to present when transferring an xray video file
    'file_xray_vid': [
    ],

    # prompts to present when transferring an "undistortion grid" file
    'file_u_grid': [
    ],

    # prompts to present when transferring an "calibration object" file
    'file_calib': [
    ]
}
