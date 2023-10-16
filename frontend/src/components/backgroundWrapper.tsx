import React from "react";
import '../styles/backgroundWrapper.css';
import VectaryEmbed from "./vectaryEmbed";


type BackgroundWrapperProps = {
  component: React.ReactNode;
};

const BackgroundWrapper: React.FC<BackgroundWrapperProps> = ({ component }) => {
    return (
        <div className="background">
            <VectaryEmbed/>
            {component}
        </div>
    );
}

export default BackgroundWrapper;
