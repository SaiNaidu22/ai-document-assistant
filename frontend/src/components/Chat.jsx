import { useState } from "react";
import api from "../services/api";
import "../styles/Chat.css";

function Chat() {

    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");
const [sources, setSources] = useState([]);
    const [loading, setLoading] = useState(false);

    const askQuestion = async () => {

        if (!question.trim()) return;

        setLoading(true);

        try {

            const response = await api.post("/chat", {
                question: question
            });

            setAnswer(response.data.answer);
            setSources(response.data.sources);

        } catch (error) {

            console.error(error);

            setAnswer("Something went wrong.");

        }

        setLoading(false);

    };

    return (

        <div className="chat-container">

            <h2>💬 Ask AI</h2>

            <textarea
                rows="3"
                placeholder="Ask something about the uploaded PDF..."
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
            />

            <button onClick={askQuestion} disabled={loading}>
    {loading ? "Thinking..." : "Ask AI"}
</button>

            {loading && <p>Thinking...</p>}

            {answer && (

                <div className="answer-box">

                    <h3>🤖 Answer</h3>

                    <p>{answer}</p>
                    {sources.length > 0 && (
    <div className="source-box">
        <h3>📚 Sources</h3>

        {sources.map((source, index) => (
            <div key={index} className="source-item">
                {source}
            </div>
        ))}
    </div>
)}

                </div>

            )}

        </div>

    );

}

export default Chat;