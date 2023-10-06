async function sendQuery(query) {
    const response = await fetch("http://localhost:5000", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ query: query }),
    });
    const data = await response.json();
    return data.response;
}

export default sendQuery