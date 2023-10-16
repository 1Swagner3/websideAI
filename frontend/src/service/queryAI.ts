async function sendQuery(query: string): Promise<string> {
    const response = await fetch("http://localhost:5000", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ query: query }),
    });

    if (!response.ok) {
        throw new Error('Network response was not ok');
    }

    const data = await response.json();

    if (!data || typeof data.response !== "string") {
        throw new Error('Unexpected response format');
    }

    return data.response;
}

export default sendQuery;
