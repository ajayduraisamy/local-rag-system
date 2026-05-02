export type Message = {
  role: "user" | "assistant";
  content: string;
};

export type QueryResponse = {
  answer: string;
  sources: string[];
};
