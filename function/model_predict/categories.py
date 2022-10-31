from enum import Enum

class EdLevel(str, Enum):
    EDLEVEL_0 = "Associate degree (A.A., A.S., etc.)"
    EDLEVEL_1 = "Bachelor’s degree (B.A., B.S., B.Eng., etc.)"
    EDLEVEL_2 = "Master’s degree (M.A., M.S., M.Eng., MBA, etc.)"
    EDLEVEL_3 = "Other doctoral degree (Ph.D., Ed.D., etc.)"
    EDLEVEL_4 = "Primary/elementary school"
    EDLEVEL_5 = "Professional degree (JD, MD, etc.)"
    EDLEVEL_6 = "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)"
    EDLEVEL_7 = "Some college/university study without earning a degree"
    EDLEVEL_8 = "Something else"


class MainBranch(str, Enum):
    MAINBRANCH_0 = "I am a developer by profession"
    MAINBRANCH_1 = "I am not primarily a developer, but I write code sometimes as part of my work"


class Country(str, Enum):
    COUNTRY_0 = "Afghanistan"
    COUNTRY_1 = "Albania"
    COUNTRY_2 = "Algeria"
    COUNTRY_3 = "Andorra"
    COUNTRY_4 = "Angola"
    COUNTRY_5 = "Argentina"
    COUNTRY_6 = "Armenia"
    COUNTRY_7 = "Australia"
    COUNTRY_8 = "Austria"
    COUNTRY_9 = "Azerbaijan"
    COUNTRY_10 = "Bahrain"
    COUNTRY_11 = "Bangladesh"
    COUNTRY_12 = "Barbados"
    COUNTRY_13 = "Belarus"
    COUNTRY_14 = "Belgium"
    COUNTRY_15 = "Benin"
    COUNTRY_16 = "Bhutan"
    COUNTRY_17 = "Bolivia"
    COUNTRY_18 = "Bosnia and Herzegovina"
    COUNTRY_19 = "Botswana"
    COUNTRY_20 = "Brazil"
    COUNTRY_21 = "Bulgaria"
    COUNTRY_22 = "Cambodia"
    COUNTRY_23 = "Cameroon"
    COUNTRY_24 = "Canada"
    COUNTRY_25 = "Cape Verde"
    COUNTRY_26 = "Chile"
    COUNTRY_27 = "China"
    COUNTRY_28 = "Colombia"
    COUNTRY_29 = "Congo, Republic of the..."
    COUNTRY_30 = "Costa Rica"
    COUNTRY_31 = "Croatia"
    COUNTRY_32 = "Cuba"
    COUNTRY_33 = "Cyprus"
    COUNTRY_34 = "Czech Republic"
    COUNTRY_35 = "Côte d'Ivoire"
    COUNTRY_36 = "Democratic Republic of the Congo"
    COUNTRY_37 = "Denmark"
    COUNTRY_38 = "Dominican Republic"
    COUNTRY_39 = "Ecuador"
    COUNTRY_40 = "Egypt"
    COUNTRY_41 = "El Salvador"
    COUNTRY_42 = "Estonia"
    COUNTRY_43 = "Ethiopia"
    COUNTRY_44 = "Fiji"
    COUNTRY_45 = "Finland"
    COUNTRY_46 = "France"
    COUNTRY_47 = "Georgia"
    COUNTRY_48 = "Germany"
    COUNTRY_49 = "Ghana"
    COUNTRY_50 = "Greece"
    COUNTRY_51 = "Guatemala"
    COUNTRY_52 = "Guinea"
    COUNTRY_53 = "Guyana"
    COUNTRY_54 = "Honduras"
    COUNTRY_55 = "Hong Kong (S.A.R.)"
    COUNTRY_56 = "Hungary"
    COUNTRY_57 = "Iceland"
    COUNTRY_58 = "India"
    COUNTRY_59 = "Indonesia"
    COUNTRY_60 = "Iran, Islamic Republic of..."
    COUNTRY_61 = "Iraq"
    COUNTRY_62 = "Ireland"
    COUNTRY_63 = "Isle of Man"
    COUNTRY_64 = "Israel"
    COUNTRY_65 = "Italy"
    COUNTRY_66 = "Jamaica"
    COUNTRY_67 = "Japan"
    COUNTRY_68 = "Jordan"
    COUNTRY_69 = "Kazakhstan"
    COUNTRY_70 = "Kenya"
    COUNTRY_71 = "Kosovo"
    COUNTRY_72 = "Kuwait"
    COUNTRY_73 = "Kyrgyzstan"
    COUNTRY_74 = "Lao People's Democratic Republic"
    COUNTRY_75 = "Latvia"
    COUNTRY_76 = "Lebanon"
    COUNTRY_77 = "Libyan Arab Jamahiriya"
    COUNTRY_78 = "Lithuania"
    COUNTRY_79 = "Luxembourg"
    COUNTRY_80 = "Madagascar"
    COUNTRY_81 = "Malawi"
    COUNTRY_82 = "Malaysia"
    COUNTRY_83 = "Maldives"
    COUNTRY_84 = "Mali"
    COUNTRY_85 = "Malta"
    COUNTRY_86 = "Mauritius"
    COUNTRY_87 = "Mexico"
    COUNTRY_88 = "Mongolia"
    COUNTRY_89 = "Montenegro"
    COUNTRY_90 = "Morocco"
    COUNTRY_91 = "Mozambique"
    COUNTRY_92 = "Myanmar"
    COUNTRY_93 = "Nepal"
    COUNTRY_94 = "Netherlands"
    COUNTRY_95 = "New Zealand"
    COUNTRY_96 = "Nicaragua"
    COUNTRY_97 = "Nigeria"
    COUNTRY_98 = "Nomadic"
    COUNTRY_99 = "Norway"
    COUNTRY_100 = "Oman"
    COUNTRY_101 = "Pakistan"
    COUNTRY_102 = "Palau"
    COUNTRY_103 = "Palestine"
    COUNTRY_104 = "Panama"
    COUNTRY_105 = "Paraguay"
    COUNTRY_106 = "Peru"
    COUNTRY_107 = "Philippines"
    COUNTRY_108 = "Poland"
    COUNTRY_109 = "Portugal"
    COUNTRY_110 = "Qatar"
    COUNTRY_111 = "Republic of Korea"
    COUNTRY_112 = "Republic of Moldova"
    COUNTRY_113 = "Romania"
    COUNTRY_114 = "Russian Federation"
    COUNTRY_115 = "Rwanda"
    COUNTRY_116 = "Saudi Arabia"
    COUNTRY_117 = "Senegal"
    COUNTRY_118 = "Serbia"
    COUNTRY_119 = "Seychelles"
    COUNTRY_120 = "Singapore"
    COUNTRY_121 = "Slovakia"
    COUNTRY_122 = "Slovenia"
    COUNTRY_123 = "Somalia"
    COUNTRY_124 = "South Africa"
    COUNTRY_125 = "South Korea"
    COUNTRY_126 = "Spain"
    COUNTRY_127 = "Sri Lanka"
    COUNTRY_128 = "Sudan"
    COUNTRY_129 = "Suriname"
    COUNTRY_130 = "Sweden"
    COUNTRY_131 = "Switzerland"
    COUNTRY_132 = "Syrian Arab Republic"
    COUNTRY_133 = "Taiwan"
    COUNTRY_134 = "Tajikistan"
    COUNTRY_135 = "Thailand"
    COUNTRY_136 = "The former Yugoslav Republic of Macedonia"
    COUNTRY_137 = "Timor-Leste"
    COUNTRY_138 = "Togo"
    COUNTRY_139 = "Trinidad and Tobago"
    COUNTRY_140 = "Tunisia"
    COUNTRY_141 = "Turkey"
    COUNTRY_142 = "Turkmenistan"
    COUNTRY_143 = "Uganda"
    COUNTRY_144 = "Ukraine"
    COUNTRY_145 = "United Arab Emirates"
    COUNTRY_146 = "United Kingdom of Great Britain and Northern Ireland"
    COUNTRY_147 = "United Republic of Tanzania"
    COUNTRY_148 = "United States of America"
    COUNTRY_149 = "Uruguay"
    COUNTRY_150 = "Uzbekistan"
    COUNTRY_151 = "Venezuela, Bolivarian Republic of..."
    COUNTRY_152 = "Viet Nam"
    COUNTRY_153 = "Yemen"
    COUNTRY_154 = "Zambia"
    COUNTRY_155 = "Zimbabwe"

