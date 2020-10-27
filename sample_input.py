sample_input = [
        {
            'v1': '1.2.3',
            'v2': '1.2.1',
            'expected_result' : 1
        },

        {
            'v1': '3.2.1',
            'v2': '1.2.3',
            'expected_result' : 1
        },

        {
            'v1': '1.2.3-alpha',
            'v2': '1.2.3-beta',
            'expected_result' : -1
        },
     
        {
            'v1': '1.2.3-alpha',
            'v2': '1.2.3',
            'expected_result' : 1
        },

        {
            'v1': '1.2.3-alpha',
            'v2': '1.2.3-alpha',
            'expected_result' : 0
        },

        {
            'v1': '1.2.3-alpha.1',
            'v2': '1.2.3-alpha.2',
            'expected_result' : -1
        },

        {
            'v1': '1.2.3-alpha.2',
            'v2': '1.2.3-alpha.1',
            'expected_result' : 1
        }

]