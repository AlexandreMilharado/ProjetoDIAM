
const Tag = ({tag,displayNumber} : {tag:Tag, displayNumber?:boolean}) => {
  return (
    <li className="tag">{tag.name} {displayNumber && tag.likeNumber}</li>
  )
}

export default Tag