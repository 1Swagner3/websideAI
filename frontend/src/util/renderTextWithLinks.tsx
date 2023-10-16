export default function renderTextWithLinks(text: string): JSX.Element {
  // This regular expression matches URLs
  const urlRegex = /https?:\/\/[^\s]+?(?=[.,!?)\]]*\s|$)/g


  // Split the text by URLs
  const parts = text.split(urlRegex);

  // Find all URLs in the text
  const matches = Array.from(text.matchAll(urlRegex));

  // Create JSX elements for each part of the text
  const elements = parts.reduce((acc, part, i) => {
    // Push the regular text
    acc.push(<span key={`part-${i}`}>{part}</span>);

    // If there's a URL after this part, push an anchor for the URL
    if (i < matches.length) {
      acc.push(
        <a href={matches[i][0]} target="_blank" rel="noopener noreferrer" key={`link-${i}`}>
          {matches[i][0]}
        </a>
      );
    }
    return acc;
  }, [] as JSX.Element[]);

  return <>{elements}</>;
}
