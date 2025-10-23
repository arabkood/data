def validateUser(user):
    errors = []

    if not user.get("name") or user["name"].strip() == "":
        errors.append("name is empty")

    age = user.get("age")
    if age is None or age < 18 or age > 100:
        errors.append("age must be between 18 and 100")

    email = user.get("email", "")
    if "@" not in email or "." not in email:
        errors.append("email must contain @ and .")

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }
