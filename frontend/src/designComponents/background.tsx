import '../styles/background.css';
import BackgroundLogo from './backgroundLogo';
import FrostedGlass from './frostedGlass';
export default function Background(){
    return (
        <div className="background">
            <BackgroundLogo/>
            <FrostedGlass/>
        </div>
    );
}