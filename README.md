## A-ML-approach-to-Malware-Dataset

##### An investigation of the use of Random Forest Classifier on the dataset provided in EMBER. Due to the computational constraints, this task was performed only on a part of the dataset.
###### The dataset consists of static features of PE32 files stored in jsonlines format.One such instance of it is shown below:
```
{'general': {'exports': 0, 
  'has_debug': 0, 
  'has_relocations': 1, 
  'has_resources': 0, 
  'has_signature': 0, 
  'has_tls': 0, 
  'imports': 41, 
  'size': 33334, 
  'symbols': 0, 
  'vsize': 45056}, 
	 'header': 	{'coff': 	{'machine': 	'I386', 
'timestamp': 1365446976}, 
  'optional': {'magic': 'PE32', 
   'major_image_version': 1, 
   'major_linker_version': 11, 
   'major_operating_system_version': 6, 
   'major_subsystem_version': 6, 
   'minor_image_version': 2, 
   'minor_linker_version': 0, 
   'minor_operating_system_version': 0, 
   'minor_subsystem_version': 0, 
   'sizeof_code': 3584, 
   'sizeof_headers': 1024, 
   'sizeof_heap_commit': 4096, 
   'subsystem': 'WINDOWS_CUI'}}, 
 'label': 1, 
 'section': {'entry': '.text', 
  'sections': [{'entropy': 6.368472139761825, 
    'name': '.text', 
    'size': 3584, 
    'vsize': 3270}, 
   {'entropy': 7.924775969038312, 
    'name': '.rdata', 
    'size': 27136, 
    'vsize': 26926}, 
	   {'entropy': 	0.9424221913195016, 	'name': 
'.data', 'size': 512, 'vsize': 528}, 
   {'entropy': 4.049286786417362, 
    'name': '.reloc', 
    'size': 1024, 
    'vsize': 514}]}, 
 'strings': {'MZ': 1, 
  'avlength': 8.170588235294117, 
  'entropy': 6.259255409240723, 
  'numstrings': 170, 
  'paths': 0, 
  'printables': 1389, 
  'registry': 0, 
  'urls': 0}} 
```
----
#### Tools used :
  ##### Python
  ##### Google Collaboratory
  ##### Flatten-json
  ##### Pandas
  ##### Numpy
  ##### scikit-learn
  ##### matplotlib
