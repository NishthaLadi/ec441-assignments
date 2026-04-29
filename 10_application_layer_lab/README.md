# Topic 10: Application Layer Lab

## Project Title
**HTTP Protocol Behavior Lab: Exploring HTTP/1.1 with curl, Python, and Timing Experiments**

## One-Line Description
Investigated HTTP/1.1 methods, status codes, headers, keep-alive behavior, and head-of-line blocking using `curl`, Python `requests`, and latency visualizations.

## Course Concepts Covered
- Application layer protocols
- HTTP/1.1 request and response format
- HTTP methods: GET, HEAD, POST, DELETE
- Status codes: 2xx, 3xx, 4xx, 5xx
- Headers: `Content-Type`, `Content-Length`, `Server`, `Date`, `Connection`
- Persistent connections / keep-alive
- Head-of-line blocking
- `curl` command-line experiments
- Python-based network measurement

## Folder Contents

```text
10_application_layer_lab/
├── README.md
├── lab_report.md
├── http_lab.py
├── requirements.txt
└── outputs/
    ├── latency_comparison.png
    ├── status_code_distribution.png
    ├── hol_blocking.png
    └── http_lab_results.csv
```

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the lab script:

```bash
python http_lab.py
```

The script will generate plots and a CSV file inside the `outputs/` folder.

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
