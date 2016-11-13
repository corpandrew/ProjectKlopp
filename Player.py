class Player:
    # league is a League
    # nation is a Nation
    # traits is an array of strings
    # specialties is an array of strings
    # attributes is an array of attribute (which has a name and value)

    def __init__(self, commonName, firstName, headshotImgUrl, lastName, league, nation, club, largeTOTWImgUrl, position,
                 playStyle, playStyleId, height, weight, birthdate, age, aggression, agility, balance, ballcontrol,
                 foot, skillMoves, crossing, curve, dribbling, finishing, freekickaccuracy, gkdiving, gkhandling,
                 gkpositioning, gkreflexes, headingaccuracy, interceptions, jumping, longpassing, longshots, marking,
                 penalties, positioning, potential, reactions, shortpassing, shotpower, slidingtackle, stamina,
                 strength, vision, volleys, weakfoot, traits, specialties, attributes, name, quality, color, isGk,
                 positionFull, isSpecialType, contracts, fitness, rawAttributeChemistryBonus, isLoan, squadPosition,
                 itemType, discardValue, id, modelName, baseId, rating):
        self.commonName = commonName
        self.firstName = firstName
        self.headshotImgUrl = headshotImgUrl
        self.lastName = lastName
        self.league = league
        self.nation = nation
        self.club = club
        self.largeTOTWImgUrl = largeTOTWImgUrl
        self.position = position
        self.playStyle = playStyle
        self.playStyleId = playStyleId
        self.height = height
        self.weight = weight
        self.birthdate = birthdate
        self.age = age
        self.aggression = aggression
        self.agility = agility
        self.balance = balance
        self.ballcontrol = ballcontrol
        self.foot = foot
        self.skillMoves = skillMoves
        self.crossing = crossing
        self.curve = curve
        self.dribbling = dribbling
        self.finishing = finishing
        self.freekickaccuracy = freekickaccuracy
        self.gkdiving = gkdiving
        self.gkhandling = gkhandling
        self.gkpositioning = gkpositioning
        self.gkreflexes = gkreflexes
        self.headingaccuracy = headingaccuracy
        self.interceptions = interceptions
        self.jumping = jumping
        self.longpassing = longpassing
        self.longshots = longshots
        self.marking = marking
        self.penalties = penalties
        self.positioning = positioning
        self.potential = potential
        self.reactions = reactions
        self.shortpassing = shortpassing
        self.shotpower = shotpower
        self.slidingtackle = slidingtackle
        self.stamina = stamina
        self.strength = strength
        self.vision = vision
        self.volleys = volleys
        self.weakfoot = weakfoot
        self.traits = traits
        self.specialties = specialties
        self.attributes = attributes
        self.name = name
        self.quality = quality
        self.color = color
        self.isGk = isGk
        self.positionFull = positionFull
        self.isSpecialType = isSpecialType
        self.contracts = contracts
        self.fitness = fitness
        self.rawAttributeChemistryBonus = rawAttributeChemistryBonus
        self.isLoan = isLoan
        self.squadPosition = squadPosition
        self.itemType = itemType
        self.discardValue = discardValue
        self.id = id
        self.modelName = modelName
        self.baseId = baseId
        self.rating = rating

    def getCommonName(self):
        return self.commonName

    def getFirstName(self):
        return self.firstName

    def getHeadshotImgUrl(self):
        return self.headshotImgUrl

    def getLastName(self):
        return self.lastName

    def getLeague(self):
        return self.league

    def getNation(self):
        return self.nation

    def getClub(self):
        return self.club

    def getLargeTOTWImgUrl(self):
        return self.largeTOTWImgUrl

    def getPosition(self):
        return self.position

    def getPlayStyle(self):
        return self.playStyle

    def getPlayStyleId(self):
        return self.playStyleId

    def getHeight(self):
        return self.height

    def getWeight(self):
        return self.weight

    def getBirthdate(self):
        return self.birthdate

    def getAge(self):
        return self.age

    def getAggression(self):
        return self.aggression

    def getAgility(self):
        return self.agility

    def getBalance(self):
        return self.balance

    def getBallcontrol(self):
        return self.ballcontrol

    def getFoot(self):
        return self.foot

    def getSkillMoves(self):
        return self.skillMoves

    def getCrossing(self):
        return self.crossing

    def getCurve(self):
        return self.curve

    def getDribbling(self):
        return self.dribbling

    def getFinishing(self):
        return self.finishing

    def getFreekickaccuracy(self):
        return self.freekickaccuracy

    def getGkdiving(self):
        return self.gkdiving

    def getGkhandling(self):
        return self.gkhandling

    def getGkpositioning(self):
        return self.gkpositioning

    def getGkreflexes(self):
        return self.gkreflexes

    def getHeadingaccuracy(self):
        return self.headingaccuracy

    def getInterceptions(self):
        return self.interceptions

    def getJumping(self):
        return self.jumping

    def getLongpassing(self):
        return self.longpassing

    def getLongshots(self):
        return self.longshots

    def getMarking(self):
        return self.marking

    def getPenalties(self):
        return self.penalties

    def getPositioning(self):
        return self.positioning

    def getPotential(self):
        return self.potential

    def getReactions(self):
        return self.reactions

    def getShortpassing(self):
        return self.shortpassing

    def getShotpower(self):
        return self.shotpower

    def getSlidingtackle(self):
        return self.slidingtackle

    def getStamina(self):
        return self.stamina

    def getStrength(self):
        return self.strength

    def getVision(self):
        return self.vision

    def getVolleys(self):
        return self.volleys

    def getWeakfoot(self):
        return self.weakfoot

    def getTraits(self):
        return self.traits

    def getSpecialties(self):
        return self.specialties

    def getAttributes(self):
        return self.attributes

    def getName(self):
        return self.name

    def getQuality(self):
        return self.quality

    def getColor(self):
        return self.color

    def getIsGk(self):
        return self.isGk

    def getPositionFull(self):
        return self.positionFull

    def getIsSpecialType(self):
        return self.isSpecialType

    def getContracts(self):
        return self.contracts

    def getFitness(self):
        return self.fitness

    def getRawAttributeChemistryBonus(self):
        return self.rawAttributeChemistryBonus

    def getIsLoan(self):
        return self.isLoan

    def getSquadPosition(self):
        return self.squadPosition

    def getItemType(self):
        return self.itemType

    def getDiscardValue(self):
        return self.discardValue

    def getId(self):
        return self.id

    def getModelName(self):
        return self.modelName

    def getBaseId(self):
        return self.baseId

    def getRating(self):
        return self.rating
