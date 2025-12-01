"use client";

import { useState } from "react";
import { askQuestion } from "@/lib/api";

export default function AskPage() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!question.trim()) return;
    setLoading(true);
    setAnswer(null);
    try {
      const res = await askQuestion(question);
      setAnswer(res.answer);
    } catch (e: any) {
      setAnswer("Error: " + e.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="p-6 max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Ask Your Course Assistant</h1>
      <textarea
        className="w-full border rounded p-2 mb-4"
        rows={4}
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask about SQL joins, lecture slides, etc."
      />
      <button
        onClick={handleAsk}
        disabled={loading}
        className="px-4 py-2 bg-blue-600 text-white rounded"
      >
        {loading ? "Thinking..." : "Ask"}
      </button>
      {answer && (
        <div className="mt-6 border rounded p-4 bg-gray-50">
          <h2 className="font-semibold mb-2">Answer</h2>
          <p>{answer}</p>
        </div>
      )}
    </main>
  );
}