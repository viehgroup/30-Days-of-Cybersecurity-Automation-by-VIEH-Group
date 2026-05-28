import dns.resolver

domain = input("Enter Domain: ")

record_types = ["A", "MX", "NS"]

for record in record_types:
    print(f"\n{record} Records:")

    try:
        answers = dns.resolver.resolve(domain, record)

        for data in answers:
            print(data)

    except Exception as e:
        print(f"Error fetching {record} records: {e}")
