import BackgroundWrapper from "./components/background";
import ChatComponent from "./components/chatComponent";


function App() {
  return (
    <>
        <BackgroundWrapper component={<ChatComponent />}></BackgroundWrapper>
    </>
  );
}

export default App;
