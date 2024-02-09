from src.ema_id_tool import ema_id


def example():
    usr_input = input("Enter your EMA-ID for validation (example: NLXYZC3KD88D0N): ")

    usr_id = ema_id.EmaID(ema_id=usr_input)

    print(f"Full ID: {usr_id.get_full_id()}")
    print(f"Full ID with dashes: {usr_id.get_full_id_with_dashes()}")
    print(f"Country code: {usr_id.country_code}")
    print(f"Provider ID: {usr_id.provider_id}")
    print(f"ID Type: {usr_id.id_type}")
    print(f"EMA instance: {usr_id.ema_instance}")
    print(f"Check digit: {usr_id.check_digit}")


example()
