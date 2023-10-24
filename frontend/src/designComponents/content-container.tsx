import ChatComponent from '../components/chatComponent';
import '../styles/content-container.css';
import ArtworkContainer from './artwork-container';
import Headline from './headline';

export default function ContentContainer(){
    return (
        <div className="content-container">
            <Headline/>
            <div className='row-container'>
                <ArtworkContainer/>
                <div className='chat-container'>
                    <ChatComponent/>
                </div> 
            </div>
        </div>
    );
}