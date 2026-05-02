"use client";

import { useState, useCallback, useEffect } from "react";
import { Message } from "@/types/chat";
import { askQuestion } from "@/lib/api";
import ChatContainer from "@/components/ChatContainer";
import ChatInput from "@/components/ChatInput";

export default function ChatPage() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [sessionId, setSessionId] = useState<string>("");

  useEffect(() => {
    setSessionId(crypto.randomUUID());
  }, []);

  const handleSend = useCallback(async (question: string) => {
    setError(null);
    const userMessage: Message = { role: "user", content: question };
    setMessages((prev) => [...prev, userMessage]);
    setIsLoading(true);

    try {
      const data = await askQuestion(question, sessionId);
      const assistantMessage: Message = {
        role: "assistant",
        content: data.answer || "No answer received.",
      };
      setMessages((prev) => [...prev, assistantMessage]);
    } catch {
      setError("Failed to get response. Please make sure the backend is running.");
      const errorMessage: Message = {
        role: "assistant",
        content: "Sorry, something went wrong. Please try again.",
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  }, [sessionId]);

  return (
    <div className="flex flex-col h-screen bg-zinc-900 text-white">
      <header className="border-b border-zinc-700 px-4 py-3">
        <h1 className="text-lg font-semibold">RAG Chat</h1>
      </header>

      <ChatContainer messages={messages} isLoading={isLoading} />

      {error && (
        <div className="px-4 py-2 bg-red-900/50 text-red-200 text-sm text-center">
          {error}
        </div>
      )}

      <ChatInput onSend={handleSend} disabled={isLoading} />
    </div>
  );
}
