import os
import random
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("outputs", exist_ok=True)

num_hosts = 50
contacts_per_host = 8

initial_requests = num_hosts * contacts_per_host
initial_broadcast_receptions = initial_requests * (num_hosts - 1)
initial_replies = initial_requests

print(f"Initial ARP requests: {initial_requests}")
print(f"Initial broadcast receptions: {initial_broadcast_receptions}")
print(f"Initial ARP replies: {initial_replies}")

def simulate_arp(num_hosts, contacts_per_host, minutes, ttl_seconds, seed=42):
    rng = random.Random(seed)
    ttl_minutes = ttl_seconds / 60

    hosts = list(range(num_hosts))
    cache = {h: {} for h in hosts}

    requests_over_time = []
    broadcast_receptions_over_time = []
    cache_hit_rate_over_time = []

    for minute in range(minutes):
        requests = 0
        cache_hits = 0
        total_contacts = 0

        # Expire cache entries
        for h in hosts:
            expired = [
                dest for dest, expiry in cache[h].items()
                if expiry <= minute
            ]
            for dest in expired:
                del cache[h][dest]

        # Generate traffic
        for h in hosts:
            destinations = rng.sample([x for x in hosts if x != h], contacts_per_host)

            for dest in destinations:
                total_contacts += 1

                if dest in cache[h]:
                    cache_hits += 1
                else:
                    requests += 1
                    cache[h][dest] = minute + ttl_minutes

                    # Destination learns source from request
                    cache[dest][h] = minute + ttl_minutes

        requests_over_time.append(requests)
        broadcast_receptions_over_time.append(requests * (num_hosts - 1))
        cache_hit_rate_over_time.append(cache_hits / total_contacts)

    return requests_over_time, broadcast_receptions_over_time, cache_hit_rate_over_time

minutes = 20
short_req, short_bcast, short_hit = simulate_arp(num_hosts, contacts_per_host, minutes, 30)
long_req, long_bcast, long_hit = simulate_arp(num_hosts, contacts_per_host, minutes, 120)

plt.figure(figsize=(9, 6))
plt.plot(short_req, marker="o", label="TTL = 30 sec")
plt.plot(long_req, marker="s", label="TTL = 120 sec")
plt.xlabel("Minute")
plt.ylabel("ARP requests")
plt.title("ARP Requests Over Time")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("outputs/arp_requests_over_time.png", dpi=200)
plt.show()

plt.figure(figsize=(9, 6))
plt.plot(short_hit, marker="o", label="TTL = 30 sec")
plt.plot(long_hit, marker="s", label="TTL = 120 sec")
plt.xlabel("Minute")
plt.ylabel("Cache hit rate")
plt.title("ARP Cache Hit Rate Over Time")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("outputs/arp_cache_hit_rate.png", dpi=200)
plt.show()

print(f"Total ARP requests, TTL=30 sec: {sum(short_req)}")
print(f"Total ARP requests, TTL=120 sec: {sum(long_req)}")
print(f"Broadcast reduction: {(1 - sum(long_req)/sum(short_req))*100:.2f}%")
