# RESULTS / PROJECT 
STATSName                                                      Stmts   Miss  Cover
-----------------------------------------------------------------------------
raindeer/__init__.py                                          0      0   100%
raindeer/argument_preprocessing.py                           76      6    92%
raindeer/data_helper.py                                      98     13    87%
raindeer/dataframe_helper.py                                 74      2    97%
raindeer/dwd_downloader.py                                   50      0   100%
raindeer/main.py                                             93     82    12%
raindeer/user_stories.py                                    225    107    52%
raindeer/utilities.py                                        33      3    91%
tests/__init__.py                                             0      0   100%
tests/argument_prepro/__init__.py                             0      0   100%
tests/argument_prepro/test_argument_prep.py                  70      3    96%
tests/data_helper/__init__.py                                 0      0   100%
tests/data_helper/test_create_url_download_list.py           37      1    97%
tests/data_helper/test_local_check.py                        34      1    97%
tests/data_helper/test_rename_function.py                    41      3    93%
tests/data_helper/test_txt_renamer.py                        24      1    96%
tests/dataframe_creator/__init__.py                           0      0   100%
tests/dataframe_creator/test_csv_writer.py                   22      1    95%
tests/dataframe_creator/test_dataframe_creator.py            21      1    95%
tests/dwd_downloader/__init__.py                              0      0   100%
tests/dwd_downloader/test_csv_writer.py                      26      1    96%
tests/dwd_downloader/test_dwd_downloader.py                  48      1    98%
tests/dwd_downloader/test_input_checker.py                    8      1    88%
tests/dwd_downloader/test_string_list_converter.py           19      1    95%
tests/dwd_downloader/test_url_checker.py                     19      1    95%
tests/integrations/__init__.py                                0      0   100%
tests/integrations/test_data_helper.py                       24      1    96%
tests/integrations/test_dataframe_helper_integration.py      57      5    91%
tests/raindear/__init__.py                                    0      0   100%
tests/raindear/tests_raindeer.py                             62      8    87%
tests/user_stories/__init__.py                                0      0   100%
tests/user_stories/test_between_years.py                     19      1    95%
tests/user_stories/test_fourier.py                           15      1    93%
tests/user_stories/test_plot_data.py                         10      1    90%
tests/user_stories/test_simple_plot.py                       16      1    94%
tests/user_stories/test_story_3.py                           17      1    94%
tests/user_stories/test_story_8.py                           27      1    96%
tests/utils/__init__.py                                       0      0   100%
tests/utils/test_yaml_reader.py                              14      1    93%
-----------------------------------------------------------------------------
TOTAL                                                      1279    250    80%
===============================================================================

Tokei results
===============================================================================
 Language            Files        Lines         Code     Comments       Blanks
===============================================================================
 Batch                   1           35           26            1            8
 Makefile                1           20            9            7            4
 Python                 41         2671         2071          199          401
 ReStructuredText        3          225          150            0           75
 Shell                   1           32           28            2            2
 Plain Text             48         5269            0         5265            4
 YAML                    1           89           79            1            9
-------------------------------------------------------------------------------
 Jupyter Notebooks       1            0            0            0            0
 |- Markdown             1           82            0           56           26
 |- Python               1           24           21            0            3
 (Total)                            106           21           56           29
-------------------------------------------------------------------------------
 Markdown                6         1162            0         1027          135
 |- BASH                 1           15           15            0            0
 |- Python               1           16            7            4            5
 (Total)                           1193           22         1031          140
===============================================================================
 Total                 103         9503         2363         6502          638
===============================================================================
