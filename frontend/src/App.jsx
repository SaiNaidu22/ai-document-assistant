import "./styles/App.css";

import Header from "./components/Header";
import Upload from "./components/Upload";
import Chat from "./components/Chat";

function App() {
    return (
        <div className="app-container">
            <Header />
            <Upload />
            <Chat />
        </div>
    );
}

export default App;