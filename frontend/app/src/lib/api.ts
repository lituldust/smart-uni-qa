const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";

export async function askQuestion(question: string) {
  const res = await fetch(`${API_BASE_URL}/api/questions`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question }),
  });

  if (!res.ok) {
    throw new Error("Failed to get answer");
  }
  return res.json() as Promise<{ answer: string; sources: any[] }>;
}