def segments_parser(output):
    lines = output.strip().split('\n')
    segments = {}
    
    for line in lines:
        segment, score = line.split(':')
        segments[segment.strip()] = int(score.strip().replace(',', ''))
    
    return segments