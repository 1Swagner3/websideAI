
import BackgroundWrapper from './components/backgroundWrapper';
import ChatComponent from './components/chatComponent';

function App() {
  return (
    <div className="App">
      <BackgroundWrapper component={<ChatComponent />}></BackgroundWrapper>
    </div>
  );
}

export default App;
