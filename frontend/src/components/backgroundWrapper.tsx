import React from "react";
import '../styles/backgroundWrapper.css';
import Logo_GLB from "./logo_glb";
import VectaryEmbed from "./vectaryEmbed";


type BackgroundWrapperProps = {
  component: React.ReactNode;
};

const BackgroundWrapper: React.FC<BackgroundWrapperProps> = ({ component }) => {
    return (
        <div className="background">
            <VectaryEmbed></VectaryEmbed>
            {component}
        </div>
    );
}

export default BackgroundWrapper;
