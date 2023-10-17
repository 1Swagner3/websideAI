
import BackgroundWrapper from './components/backgroundWrapper';
import ChatComponent from './components/chatComponent';
import Background from './designComponents/background';

function App() {
  return (
    <div className="App">
      {/* <BackgroundWrapper component={<ChatComponent />}></BackgroundWrapper> */}
      <Background/>
    </div>
  );
}

export default App;
