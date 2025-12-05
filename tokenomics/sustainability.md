# Sustainability & Value Loop

A sustainable token economy requires strong demand and deflationary mechanisms. **12cycle** introduces the **"Cycle of Value"** to protect the token price.

![Value Loop Diagram Placeholder](Placeholders/value_loop.png)

## 🔥 Deflationary Mechanisms (Burn)

To combat inflation, we implement systematic token burning:

1.  **IP Licensing Fees:**
    * Whenever a third-party company uses the 12 Zodiac IP, the licensing fee is paid in **12C** and **permanently burned**.
2.  **Marketplace Tax:**
    * A 2.5% fee on all NFT trades is collected. 50% is burned, and 50% goes to the Treasury.
3.  **Gacha/Random Box:**
    * Using **12C** to open limited edition character boxes removes tokens from circulation.

## 💰 Revenue Stream
The project generates revenue through **In-Game Purchases**, **Media Contents**, and **Physical Goods**. As the universe expands, the circulating supply decreases.

---

## 📉 Inflation & Deflation Strategy

### Token Emission Formula

12cycle maintains economic stability through a dynamic emission rate adjustment mechanism.

$$
F_{emit} = R_{base} \\times (1 - B_{rate}) \\times M_{activity}
$$

**Variable Definitions:**
- $F_{emit}$: Actual Emission
- $R_{base}$: Base Reward Rate
- $B_{rate}$: Burn Rate
- $M_{activity}$: Activity Multiplier (0.5 ~ 2.0)

### Emission Schedule

**Ecosystem Rewards Pool (40%, 4,800,000,000 12C)** annual emission plan:

| Year | Emission (12C) | Cumulative % | Primary Use |
|------|-------------|-----------|----------|
| Year 1 | 960,000,000 | 20% | Initial user acquisition & PoC rewards |
| Year 2 | 720,000,000 | 35% | Game launch and expansion |
| Year 3 | 576,000,000 | 47% | Global expansion |
| Year 4 | 480,000,000 | 57% | Metaverse integration |
| Year 5+ | 384,000,000/year | Declining rate | Sustainable rewards |

**Emission Reduction Curve:**

```
Year 1: 100% baseline
Year 2: -25% (0.75x)
Year 3: -20% (0.80x of Year 2)
Year 4: -17% (0.83x of Year 3)
Year 5+: -20% annual reduction (Half-life: 5 years)
```

### Burn Mechanism Details

#### Automatic Burn Triggers

**1. Transaction Fee Burns**

```
2.5% of NFT marketplace transaction volume
→ 1.25% immediate burn
→ 1.25% to DAO Treasury

Assuming $1M monthly volume:
Annual burn: $150,000 equivalent in 12C
```

**2. IP Licensing Burns**

```
100% corporate IP usage fees paid in 12C
→ Complete permanent burn

Projected licensing:
- Gaming partnerships: $500K-2M annually
- Merchandise manufacturers: $200K-500K annually
- Media collaborations: $100K-300K annually
```

**3. Premium Feature Burns**

| Feature | Burn Rate | Estimated Annual Burn |
|------|----------|----------------|
| Gacha/Random Box | 100% | 300M 12C |
| Premium Webtoon Unlock | 70% | 150M 12C |
| Name Change | 100% | 50M 12C |
| Special Skin Purchase | 50% | 100M 12C |

#### Burn Acceleration Conditions

Burn rate automatically adjusts based on ecosystem health:

```python
if circulation_ratio > 0.7:  # If circulation exceeds 70% of total supply
    burn_rate = base_burn_rate * 1.5
elif circulation_ratio < 0.4:  # If below 40%
    burn_rate = base_burn_rate * 0.7
else:
    burn_rate = base_burn_rate
```

### Deflationary Threshold

**Target:** Achieve net deflation from Year 3 onwards

$$
\\text{Net Supply Change} = F_{emit} - F_{burn}
$$

**Simulation Results:**

| Year | Emission | Burn (Projected) | Net Change |
|------|--------|--------------|---------|
| Year 1 | 960M | 200M | +760M (Net Increase) |
| Year 2 | 720M | 400M | +320M (Net Increase) |
| Year 3 | 576M | 600M | **-24M (Net Decrease)** ✅ |
| Year 4 | 480M | 800M | **-320M (Net Decrease)** ✅ |
| Year 5 | 384M | 1,000M | **-616M (Net Decrease)** ✅ |

---

## 📊 Vesting Schedule

### Team Allocation (10%, 1,200,000,000 12C)

**Lock-up Terms:**
- TGE: 0% (Fully locked)
- 6-month Cliff: No rewards
- 36-month Linear Vesting

```
Month 0-6: 0 12C (Cliff Period)
Month 7: 33,333,333 12C (First unlock)
Month 8-42: 33,333,333 12C monthly (Linear unlock)
Total: 36-month distribution
```

**베스팅 그래프:**

```
1,200M ┤                                        ████████
        │                                  ██████
        │                            ██████
        │                      ██████
        │                ██████
        │          ██████
        │    ██████
        │____
        0    6    12   18   24   30   36   42 (months)
```

### Advisor Allocation (Separate from Team Pool, 200,000,000 12C)

**Lock-up Terms:**
- TGE: 10% (Immediate unlock as early contribution reward)
- 12-month Linear Vesting

```
TGE: 20,000,000 12C (10%)
Month 1-12: 15,000,000 12C monthly (90% distribution)
```

### Private/Public Sale (5%, 600,000,000 12C)

#### Private Sale (3%, 360,000,000 12C)

**Terms:**
- Price: $0.005/12C
- TGE: 5% (18,000,000 12C)
- 6-month Cliff
- 18-month Linear Vesting

| Period | Unlock Amount | Cumulative % |
|------|--------|----------|
| TGE | 18M | 5% |
| Month 7-24 | 19M monthly | 95% distribution |

#### Public Sale (2%, 240,000,000 12C)

**Terms:**
- Price: $0.008/12C
- TGE: 10% (24,000,000 12C)
- 3-month Cliff
- 9-month Linear Vesting

| Period | Unlock Amount | Cumulative % |
|------|--------|----------|
| TGE | 24M | 10% |
| Month 4-12 | 24M monthly | 90% distribution |

### Ecosystem Rewards (40%, 4,800,000,000 12C)

**Distribution Method:**
- Automated smart contract management
- Real-time distribution based on PoC activity verification
- Annual emission cap applied (refer to emission schedule above)

### Development Fund (20%, 2,400,000,000 12C)

**Lock-up Terms:**
- Managed by DAO multi-sig wallet
- Quarterly usage plans disclosed to community
- Transparent post-usage reports submitted

| Quarter | Available Amount | Primary Use |
|------|-----------|----------|
| Q1-Q4 | 100M per quarter | Platform development, infrastructure |
| Year 2 | 120M per quarter | IP expansion, new content |
| Year 3+ | 80M per quarter | Maintenance, upgrades |

### Marketing Fund (15%, 1,800,000,000 12C)

**Distribution Strategy:**
- Year 1: 40% (720M) - Initial brand awareness
- Year 2: 30% (540M) - Global expansion
- Year 3+: 30% (540M) - Sustained branding

### Reserve Fund (10%, 1,200,000,000 12C)

**Purpose:**
- Emergency liquidity provision
- Exchange market making
- Response to unexpected market volatility

**Lock-up:**
- Cannot be used without DAO vote
- Requires minimum 5/7 multi-sig approval

---

## 📈 Price Stability Mechanism

### Automated Market Maker (AMM) Strategy

**Liquidity Pool Management:**

```
Initial Liquidity: $500K (12C/ETH pair)
→ Protocol fee 0.3%
→ 100% fee reinvestment for liquidity growth

Target Liquidity: Year 2 $5M
```

### Price Floor Mechanisms

1. **Automated Buyback Program**

```
Condition: 7-day moving average drops 50% below launch price
Execution: Weekly maximum $50K purchases from Treasury
Burn: 100% immediate burn of purchased tokens
```

2. **Emergency Staking Boost**

```
Condition: Price hits 30-day low
Execution: All staking APY doubled for 1 week
Effect: Reduced circulation for price stabilization
```

### Token Economics Monitoring Metrics

**Core KPIs:**

| Metric | Target | Warning Level |
|------|--------|--------|
| Daily Trading Volume | > $100K | < $20K |
| Holder Count | Quarterly +20% | Declining trend |
| Staking Ratio | > 30% | < 15% |
| Burn Rate | Annual 5%+ | < 2% |

**Monthly Transparency Reports:**
- Emission and burn volumes disclosed
- Major wallet movement analysis
- Ecosystem activity metrics
- Next month's projected supply changes
