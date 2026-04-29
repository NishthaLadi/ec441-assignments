# Topic 10: Application Layer Lab

## Lab Project Title
**HTTP Protocol Behavior Lab: Exploring HTTP/1.1 with curl, Python, and Timing Experiments**

## One-Line Description
Investigated HTTP/1.1 methods, status codes, headers, keep-alive behavior, and head-of-line blocking using `curl`, Python `requests`, and latency visualizations.

## Curl Commands Used

### Basic HTTP GET

```bash
curl -v --http1.1 https://example.com
```

### HEAD Request

```bash
curl -I --http1.1 https://example.com
```

### Status Codes

```bash
curl -I https://httpbin.org/status/200
curl -I https://httpbin.org/status/301
curl -I https://httpbin.org/status/404
curl -I https://httpbin.org/status/500
```

### POST Request

```bash
curl -X POST https://httpbin.org/post -d "name=EC441"
```

## Main Experiments

1. Compare HTTP response behavior across methods.
2. Analyze status code categories.
3. Measure latency with and without persistent sessions.
4. Simulate head-of-line blocking using delayed HTTP endpoints.
5. Plot and interpret application-layer timing behavior.

## Expected Outputs

- `latency_comparison.png`: compares requests with and without `requests.Session()`.
- `status_code_distribution.png`: shows the distribution of observed HTTP status codes.
- `hol_blocking.png`: compares sequential delayed requests against parallel delayed requests.
- `http_lab_results.csv`: stores measured latency and experiment metadata.

## Key Takeaway
HTTP/1.1 improves efficiency through persistent connections, but sequential request handling can still create head-of-line blocking when one slow response delays later responses.
