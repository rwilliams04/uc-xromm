config = {

    # info about the config file (version, change history, etc)
    'meta': {
        'version': "0.0.3",         # increment version whenever making changes 
        'changes': [                # note changes
            ('2015-04-27', "corrected formatting errors")
        ],
        'prompt_subseq': {          # prompt subsequence choices
            'study': [],            # no subseqs for studies
            'trial': [
                'trial_regular',
                'trial_calibration'
            ],
            'file_transfer': [
                'file_u_grid',
                'file_calib',
                'file_xray_vid',
                'file_std_vid',
                'file_emg',
                'file_misc',
                'file_proc_data',
                'file_3d_vol'
            ]
        }
    },  # END META

    # prompts to present when creating a new study
    'study': [
        [
            'open',                  # prompt type (open|enum_open|enum|bool)
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
            'open',                 # prompt types
            'desc',                 # key name for json output
            'Description of study?', # prompt 
            '''
            Please provide a short description of the purpose and aim of 
            this study.
            ''',                    # extra usage/help/info/examples
            [],                     # enumerated options (or null list if none)
            r'\w{3}'                # regex for sanity check on input
        ],
        [
            'enum',                 # prompt type
            'pi',                   # key name for json output
            'Name of Principal Investigator?', #prompt
            '',                     # extra usage/help/info/examples
            ['Callum Ross'],        # enumerated option
            r'^\d$'                 # input must be numeric w/ enum options
        ],
        [
	    'enum',                 # prompt type
            'leader',               # key name for json output
            'Name of study leader?', # prompt
            '''
            The lab member most responsible for conducting this
            study.
            ''',                    # extra usage/help/info/examples
            ['Callum Ross', 'Kazutaka Takashi'],  # enumerated option 
            r'^\d$'                 # input must be numeric w/ enum options
        ],
        [   
	    'bool',                 # prompt type
            'meta_public',          # key name for json output
            'Metadata for this study is public? (y|n)', #prompt
            '''
            Can the metadata for this study be made publicly available?
            Use `y` for yes or `n` for no.
            ''',                    # extra usage/help/info/examples
            ['y', 'n'],             # boolean options
            r'^[yn]$'               # regex for sanity check on input
        ],
        [
            'bool',                 # prompt type
            'data_public',          # key name for json output
            'Data for this study is public? (y|n)', # prompt
            '''
            Can the data files for this study be made publicly available?
            Use `y` for yes or `n` for no.
            ''',                    # extra usage/help/info/examples
            ['y', 'n'],             # boolean options
            r'^[yn]$'               # regex for sanity check on input
        ],
        [
            'open',                 # prompt type
            'notes',                # key name for json output
            'Additional notes or comments? (hit return for none)', # prompt
            '''
            Here you can provide additional info pertaining to this study
            that might be useful for future reference.
            ''',                    # extra usage/help/info/examples
            [],                     # null list
            r'\w?'                  # regex for sanity check on input
        ]
    ],

    # prompt to present when creating a new trial
    'trial': [
        [
            'enum_fixed',            # prompt type
            'type',                  # key name for json output
            'Type of trial?',        # prompt
            '''
            Enter "1" for regular trials. Enter "2" for calibration trials
            ''',                     # extra usage/help/info/examples
            ['regular', 'calibration'],  # trial type list
            r'^[1-2]$'               # regex for sanity check on input
        ]
    ],

    # prompts to present when creating a regular trial
    'regular_trial': [
        [
            'open',                  # prompt type
            'name',                  # key name for json output
            'Trial name? (max 50 chars)', # prompt
            "Name of this trial?",          # extra usage/examples/info
            [],                      # null list
            r'\w[a-z_ ]+'            # regex for sanity check on input
        ],
        [
            'open',                  # prompt type
            'date',                  # key name for json output
            'Trial date? (YYYY/MM/DD)',  # prompt
            "Date of this trial?",   # extra usage/examples/info
            [],                      # null list
            r'^20\d{2}/\d{2}/\d{2}'  # regex for sanity check on input
        ]
    ],

    # prompts to present when creating a calibration trial
    'calibration_trial': [
        [
            'open',                  # prompt type
            'name',                  # key name for json output
            'Trial name? (max 50 chars)', # prompt
            "Name of this trial?",   # extra usage/examples/info
            [],                      # null list
            r'\w[a-z_ ]+'            # regex for sanity check on input
        ],
        [
            'open',                  # prompt type
            'date',                  # key name for json output
            'Trial date? (YYYY/MM/DD)',   # prompt
            "Date of this trial?",   # extra usage/examples/info
            [],                      # null list
            r'^20\d{2}/\d{2}/\d{2}'  # regex for sanity check on input
        ]
    ],

    # prompts to present when transferring a data file
    'file_transfer': [
        [
            'enum_fixed',            # prompt type
            'filetype',              # key name for json output
            'Type of file?',         # prompt
            "Please choose one of the enumerated options.",
            [ 
                ("Undistortion Grid", 'file_u_grid'), # Calibration trial only
                ("Calibration Object", 'file_calib'), # Calibration trial only
		("X-Ray Video", 'file_xray_vid'),     # Regular trial only
                ("Standard Video", 'file_std_vid'),   # Regular trial only
		("EMG File", 'file_emg'),             # Regular trial only
		("Misc. File", 'file_misc'),          # Either trial type
		("Proc. Data", 'file_proc_data'),      # Either trial type
		("3D Vol.", 'file_3d_vol')           # Subject must be selected (not linked to trial)
            ],                       # extra usage/examples/info
            r'^[1-7]$'               # regex for sanity check on input
        ]
    ],


    # prompts to present when transferring an "undistortion grid" file
    'file_u_grid': [
	[
            'enum_open',             # prompt type
            'trial_select',          # key name for json output
            'Select calibration trial:', # prompt
	    "Select calibration trial from enumerated list",  # extra usage/examples/info
            r'^\d$'                  # input must be numeric w/ enum options
	],
	[
            'enum_fixed',            # prompt type
            'camera'                 # key name for json output
            'Select camera:'         # prompt
            "Select camera from enumerated list", # extra usage/examples/info
	    r'^[1-4]$'               # regex for sanity check on input  
	],
	[
            'open',                  # prompt type
            'file_select',           # key name for json output
            "Enter file name:",      # prompt
	    '''
            Enter name of file. The file name will be compared against
            the names of files in relevant directory.
            ''',                     # extra usage/examples/info 
            r'\w[a-z_ ]+'            # regex for sanity check on input
	]
    ],

    # prompts to present when transferring an "calibration object" file
    'file_calib': [
        [
            'enum_open',             # prompt type
            'trial_select',          # key name for json output
            'Select calibration trial:', # prompt
            "Select calibration trial from enumerated list",  # extra usage/examples/info
            r'^\d$'                  # input must be numeric w/ enum options
        ],
        [
            'enum_fixed',            # prompt type
            'camera'                 # key name for json output
            'Select camera:'         # prompt
            "Select camera from enumerated list", # extra usage/examples/info
            r'^[1-4]$'               # regex for sanity check on input
        ],
        [
            'open',                  # prompt type
            'file_select',           # key name for json output
            "Enter file name:",      # prompt
            '''
            Enter name of file. The file name will be compared against
            the names of files in relevant directory.
            ''',                     # extra usage/examples/info
            r'\w[a-z_ ]+'            # regex for sanity check on input
        ]
    ],


    # prompts to present when transferring an xray video file
    'file_xray_vid': [
	[
            'enum_open',             # prompt type
            'trial_select',          # key name for json output
            'Select regular trial:', # prompt
	    "Select regular trial from enumerated list",  # extra usage/examples/info
            r'^\d$'                  # input must be numeric w/ enum options
	],
	[
            'enum_fixed',            # prompt type
            'camera'                 # key name for json output
            'Select camera:'         # prompt
            "Select camera from enumerated list", # extra usage/examples/info
	    r'^[1-4]$'               # regex for sanity check on input
	],  
	[
            'open',                  # prompt type
            'file_select',           # key name for json output
            "Enter file name:",      # prompt
	    '''
            Enter name of file. The file name will be compared against
            the names of files in relevant directory.
            ''',                     # extra usage/examples/info 
            r'\w[a-z_ ]+'            # regex for sanity check on input
	]
    ],

    
    # prompts to present when transferring a standard video file
    'file_std_vid': [
        [
            'enum_open',             # prompt type
            'trial_select',          # key name for json output
            'Select regular trial:', # prompt
            "Select regular trial from enumerated list",  # extra usage/examples/info
            r'^\d$'                  # input must be numeric w/ enum options
        ],
        [
            'enum_fixed',            # prompt type
            'camera'                 # key name for json output
            'Select camera:'         # prompt
            "Select camera from enumerated list", # extra usage/examples/info
            r'^[1-4]$'               # regex for sanity check on input
        ],
        [
            'open',                  # prompt type
            'file_select',           # key name for json output
            "Enter file name:",      # prompt
            '''
            Enter name of file. The file name will be compared against
            the names of files in relevant directory.
            ''',                     # extra usage/examples/info
            r'\w[a-z_ ]+'            # regex for sanity check on input
        ]
    ],

    # prompts to present when transferring an emg file
    'file_emg': [
        [
            'enum_open',             # prompt type
            'trial_select',          # key name for json output
            'Select regular trial:', # prompt
            "Select regular trial from enumerated list",  # extra usage/examples/info
            r'^\d$'                  # input must be numeric w/ enum options
        ],
        [
            'open',                  # prompt type
            'file_select',           # key name for json output
            "Enter file name:",      # prompt
            '''
            Enter name of file. The file name will be compared against
            the names of files in relevant directory.
            ''',                     # extra usage/examples/info
            r'\w[a-z_ ]+'            # regex for sanity check on input
        ]
    ],

    # prompts to present when transferring a misc. file
    'file_misc': [
        [
            'enum_open',             # prompt type
            'trial_select',          # key name for json output
            'Select regular trial:', # prompt
            "Select regular trial from enumerated list",  # extra usage/examples/info
            r'^\d$'                  # input must be numeric w/ enum options
        ],
        [
            'open',                  # prompt type
            'file_select',           # key name for json output
            "Enter file name:",      # prompt
            '''
            Enter name of file. The file name will be compared against
            the names of files in relevant directory.
            ''',                     # extra usage/examples/info
            r'\w[a-z_ ]+'            # regex for sanity check on input
        ]
    ],

    # prompts to present when transferring a proc. file
    'file_proc': [
        [
            'enum_open',             # prompt type
            'trial_select',          # key name for json output
            'Select regular trial:', # prompt
            "Select regular trial from enumerated list",  # extra usage/examples/info
            r'^\d$'                  # input must be numeric w/ enum options
        ],
        [
            'open',                  # prompt type
            'file_select',           # key name for json output
            "Enter file name:",      # prompt
            '''
            Enter name of file. The file name will be compared against
            the names of files in relevant directory.
            ''',                     # extra usage/examples/info
            r'\w+'            # regex for sanity check on input
        ]
    ],

    # prompts to present when transferring a 3D volume file
    'file_3d_vol': [
        [
            'enum_open',             # prompt type
            'subject',               # key name for json output
            'Name of subject?',      # prompt
            "Select subject from enumerated list",  # extra usage/examples/info
            r'^\d$'                  # input must be numeric w/ enum options
        ],
        [
            'open',                  # prompt type
            'file_select',           # key name for json output
            "Enter file name:",      # prompt
            '''
            Enter name of file. The file name will be compared against
            the names of files in relevant directory.
            ''',                     # extra usage/examples/info
            r'\w+'                   # regex for sanity check on input
        ]
    ],

    # more filetypes to add here? if so, add `file_TYPE` to the 
    # enumerated options for the `file_transfer` prompt above.
    # 'file_TYPE': [ PROMPTS ]
}
