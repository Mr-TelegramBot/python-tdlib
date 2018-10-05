from ..factory import Method, Type


class passportElementPersonalDetails(Type):
    # A Telegram Passport element containing the user's personal details @personal_details
    # Personal details of the user

    personal_details = None  # type: "personalDetails"


class passportElementPassport(Type):
    # A Telegram Passport element containing the user's passport @passport Passport

    passport = None  # type: "identityDocument"


class passportElementDriverLicense(Type):
    # A Telegram Passport element containing the user's driver license @driver_license Driver license

    driver_license = None  # type: "identityDocument"


class passportElementIdentityCard(Type):
    # A Telegram Passport element containing the user's identity card @identity_card Identity card

    identity_card = None  # type: "identityDocument"


class passportElementInternalPassport(Type):
    # A Telegram Passport element containing the user's internal passport @internal_passport Internal passport

    internal_passport = None  # type: "identityDocument"


class passportElementAddress(Type):
    # A Telegram Passport element containing the user's address @address Address

    address = None  # type: "address"


class passportElementUtilityBill(Type):
    # A Telegram Passport element containing the user's utility bill @utility_bill Utility bill

    utility_bill = None  # type: "personalDocument"


class passportElementBankStatement(Type):
    # A Telegram Passport element containing the user's bank statement @bank_statement Bank statement

    bank_statement = None  # type: "personalDocument"


class passportElementRentalAgreement(Type):
    # A Telegram Passport element containing the user's rental agreement @rental_agreement Rental agreement

    rental_agreement = None  # type: "personalDocument"


class passportElementPassportRegistration(Type):
    # A Telegram Passport element containing the user's passport registration pages
    # @passport_registration Passport registration pages

    passport_registration = None  # type: "personalDocument"


class passportElementTemporaryRegistration(Type):
    # A Telegram Passport element containing the user's temporary registration @temporary_registration Temporary registration

    temporary_registration = None  # type: "personalDocument"


class passportElementPhoneNumber(Type):
    # A Telegram Passport element containing the user's phone number @phone_number Phone number

    phone_number = None  # type: "string"


class passportElementEmailAddress(Type):
    # A Telegram Passport element containing the user's email address @email_address Email address

    email_address = None  # type: "string"


class getPassportElement(Method):
    # Returns one of the available Telegram Passport elements @type Telegram
    # Passport element type @password Password of the current user

    type = None  # type: "PassportElementType"
    password = None  # type: "string"


class setPassportElement(Method):
    # Adds an element to the user's Telegram Passport. May return
    # an error with a message "PHONE_VERIFICATION_NEEDED" or "EMAIL_VERIFICATION_NEEDED" if the
    # chosen phone number or the chosen email address must be
    # verified first @element Input Telegram Passport element @password Password of the current user

    element = None  # type: "InputPassportElement"
    password = None  # type: "string"
