type TableEntry = { 'id'? : number }

type User = TableEntry & {
    username : string,
    email : string,
    isSuperUser: boolean,
    birthDay? : Date,
    profilePicture?:string,
    favoritesPlaces? : Place[]
}

type Place = TableEntry & {
    title : string,
    rating : number,
    description : string,
    location : string,
    reviewNumber : number,
    mainImage : string,
    userId? : number,
    reviews? : Review[]
    tags? : Tag[] 
}

type Tag = TableEntry & {
    name : string,
    likeNumber?: number
}

type Review = TableEntry & {
    placeId : number,
    comment : string,
    rating  : string,
    userId : string,
    date : Date,
}