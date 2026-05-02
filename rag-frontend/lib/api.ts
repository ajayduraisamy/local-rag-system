export async function askQuestion(question: string, sessionId: string) {
  const res = await fetch("http://localhost:8000/query/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ question, session_id: sessionId })
  });


  if (!res.ok) {
    throw new Error("Failed to fetch response from backend");
  }

  return res.json();
}
