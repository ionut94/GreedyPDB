(define (problem grounded-STRIPS-DEMO)
(:domain grounded-STRIPS-DMS)
(:init
(do-normal)
(= (total-cost) 0)
(NOT-AUTHENTICATED-BOB_UID-YETI)
(NOT-AUTHENTICATED-ADAM_UID-BIGFOOT)
(NOT-AUTHENTICATED-GREG_UID-SHERPA)
(NOT-HAS_PROCESS-YETI-PROC_0)
(NOT-HAS_PROCESS-YETI-PROC_1)
(NOT-HAS_PROCESS-YETI-PROC_2)
(NOT-HAS_PROCESS-YETI-PROC_3)
(NOT-HAS_PROCESS-BIGFOOT-PROC_0)
(NOT-HAS_PROCESS-BIGFOOT-PROC_1)
(NOT-HAS_PROCESS-BIGFOOT-PROC_2)
(NOT-HAS_PROCESS-BIGFOOT-PROC_3)
(NOT-HAS_PROCESS-SHERPA-PROC_0)
(NOT-HAS_PROCESS-SHERPA-PROC_1)
(NOT-HAS_PROCESS-SHERPA-PROC_2)
(NOT-HAS_PROCESS-SHERPA-PROC_3)
(NOT-TRANSMITTED-EMAIL_1)
(NOT-RECIPIENT-EMAIL_1-BOB_UID)
(NOT-RECIPIENT-EMAIL_1-ADAM_UID)
(NOT-RECIPIENT-EMAIL_1-GREG_UID)
(NOT-EMAIL_CONTENTS-EMAIL_1-BOB_PWD)
(NOT-EMAIL_CONTENTS-EMAIL_1-BOB_DMS_PWD)
(NOT-EMAIL_CONTENTS-EMAIL_1-BOB_PGP_PWD)
(NOT-EMAIL_CONTENTS-EMAIL_1-ADAM_PWD)
(NOT-EMAIL_CONTENTS-EMAIL_1-ADAM_DMS_PWD)
(NOT-EMAIL_CONTENTS-EMAIL_1-NES_ADMIN_PASS)
(NOT-EMAIL_CONTENTS-EMAIL_1-GREG_PWD)
(NOT-EMAIL_CONTENTS-EMAIL_1-GREG_DMS_PWD)
(NOT-EMAIL_CONTENTS-EMAIL_1-SECRET_INFO)
(NOT-FILE_CONTENTS_PROGRAM-NEW_FILE-NEW_VIRUS)
(NOT-FILE_CONTENTS_PROGRAM-NEW_FILE-NEW_INJECTOR)
(NOT-FILE_CONTENTS_PROGRAM-NEW_FILE-IE_VIRUS)
(NOT-FILE_CONTENTS_PROGRAM-Y_IEXPLORE-NEW_VIRUS)
(NOT-FILE_CONTENTS_PROGRAM-Y_IEXPLORE-IE_VIRUS)
(NOT-FILE_CONTENTS_PROGRAM-B_IEXPLORE-NEW_VIRUS)
(NOT-FILE_CONTENTS_PROGRAM-B_IEXPLORE-IE_VIRUS)
(NOT-FILE_CONTENTS_PROGRAM-S_IEXPLORE-NEW_VIRUS)
(NOT-MANDATORY_STEP-NOBODY)
(NOT-MANDATORY_STEP-BOB)
(NOT-MANDATORY_STEP-ADAM)
(NOT-MANDATORY_STEP-GREG)
(NOT-CONNECTING-DMSS1)
(NOT-CONNECTING-DMSS2)
(NOT-CONNECTED-DMSS1)
(NOT-CONNECTED-DMSS2)
(NOT-DMS_ESTABLISHED-DMSS1)
(NOT-DMS_ESTABLISHED-DMSS2)
(NOT-HOST_LOCKED-YETI)
(NOT-HOST_LOCKED-BIGFOOT)
(NOT-HOST_LOCKED-SHERPA)
(NOT-IS_KEYLOGGED-YETI-KEYCAP)
(NOT-AT_HOST-BOB-YETI)
(NOT-AT_HOST-ADAM-BIGFOOT)
(NOT-AT_HOST-ADAM-EVEREST)
(NOT-AT_HOST-GREG-SHERPA)
(NOT-FILE_ENCRYPTED-NEW_FILE-BOB_PGP_KEY)
(NOT-FILE_ENCRYPTED-NEW_FILE-GREG_PGP_KEY)
(NOT-FILE_ENCRYPTED-Y_IEXPLORE-BOB_PGP_KEY)
(NOT-FILE_ENCRYPTED-Y_IEXPLORE-GREG_PGP_KEY)
(NOT-FILE_ENCRYPTED-B_IEXPLORE-BOB_PGP_KEY)
(NOT-FILE_ENCRYPTED-B_IEXPLORE-GREG_PGP_KEY)
(NOT-FILE_ENCRYPTED-S_IEXPLORE-BOB_PGP_KEY)
(NOT-FILE_ENCRYPTED-S_IEXPLORE-GREG_PGP_KEY)
(AT_HOST-NOBODY-EVEREST)
(CONSOLE_USER-NOBODY-NOUID-SHERPA)
(AT_HOST-NOBODY-SHERPA)
(INST_BY-GREG_INST-NOBODY)
(KNOWS-GREG-GREG_DMS_PWD)
(CONSOLE_USER-NOBODY-NOUID-BIGFOOT)
(AT_HOST-NOBODY-BIGFOOT)
(KNOWS-ADAM-ADAM_DMS_PWD)
(CONSOLE_USER-NOBODY-NOUID-YETI)
(AT_HOST-NOBODY-YETI)
(INST_BY-MANDATORY_UPDATE-NOBODY)
(KNOWS-BOB-BOB_DMS_PWD)
(PMODE-M_FREE)
(IN_ROOM-KEY_0-ADAMS_OFFICE)
(KNOWS-ADAM-GREG_DMS_PWD)
(HAS_KEYLOGGER-BOB-KEYCAP)
)
(:goal
(and
(do-normal)
(KNOWS-BOB-SECRET_INFO)
(MANDATORY_STEP-BOB)
)
)
(:metric minimize (total-cost))
)
