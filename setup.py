import os

# 생성할 파일들과 그 내용 정의
files = {
    "README.md": """# Welcome to 12cycle

![12cycle Banner Placeholder](Placeholders/main_banner.png)

> **"Connecting Cultures, Cycling Value"**

**12cycle** is a blockchain-based cultural project that reinterprets the traditional **12 Zodiacs** into a universal standard. We aim to create a borderless digital culture ecosystem where anyone, from any background, can participate and prove their cultural contributions.

## 🌟 Why 12cycle?

The cultural industry faces fragmentation and lack of transparency. **12cycle** solves this by using blockchain technology to create a **"Proof of Culture"** protocol.

{% hint style="info" %}
**Key Concept:**
The **12cycle Coin** is not just a currency; it serves as **evidence** of your participation in the cultural ecosystem—whether it's gaming, creating webtoons, or collecting digital assets.
{% endhint %}

## 🚀 Key Features

* **Universal IP:** 12 Zodiac characters designed to resonate across Asian, Western, and global cultures.
* **Scalability:** From Webtoons and Games to the Metaverse and Physical Goods.
* **Transparency:** All cultural contributions and rewards are recorded on-chain.

## 🔗 Quick Links

| Section | Description |
| :--- | :--- |
| [**Ecosystem**](ecosystem/mechanism.md) | Understand how the "Proof of Culture" works. |
| [**Tokenomics**](tokenomics/allocation.md) | View the allocation and vesting schedule. |
| [**Roadmap**](roadmap/roadmap.md) | Check our journey and future plans. |
""",

    "SUMMARY.md": """# Table of contents

* [Welcome to 12cycle](README.md)

## 🌏 The Ecosystem
* [Proof of Culture](ecosystem/mechanism.md)

## 💎 Token Economy
* [Allocation & Vesting](tokenomics/allocation.md)

## 🗺️ Roadmap
* [Development Plan](roadmap/roadmap.md)
""",

    "ecosystem/mechanism.md": """# Proof of Culture

The core mechanism of the 12cycle ecosystem is the **"Proof of Culture" (PoC)**. This mechanism transforms user engagement into tangible value.

![Ecosystem Flowchart Placeholder](Placeholders/ecosystem_flow.png)

## 🧬 How It Works

Unlike traditional platforms where user data is siloed, 12cycle verifies and rewards cultural activities across applications.

1.  **Participation:** Users play 12cycle-IP games or read webtoons.
2.  **Verification:** The activity is verified on-chain as a "Cultural Transaction."
3.  **Reward:** Users earn **12C tokens** as proof of their contribution.

> 💡 **Utility:** The earned 12C tokens act as a "Ticket" or "Passport" to access higher-tier content, exclusive merchandise, and governance rights within the DAO.
""",

    "tokenomics/allocation.md": """# Allocation & Vesting

The **12cycle (12C)** token economy is designed to ensure long-term sustainability and value circulation. The number **12** is symbolic and central to our mathematical modeling.

## 📊 Token Overview

| Feature | Detail |
| :--- | :--- |
| **Token Name** | 12cycle |
| **Symbol** | 12C |
| **Total Supply** | 12,000,000,000 12C |
| **Network** | Ethereum / Polygon (TBD) |

## 🥧 Distribution

![Token Allocation Pie Chart](Placeholders/allocation_chart.png)

| Category | Percentage | Amount (12C) | Description |
| :--- | :--- | :--- | :--- |
| **Ecosystem & Rewards** | **40%** | 4,800,000,000 | Rewards for "Proof of Culture" participants. |
| **Development** | **20%** | 2,400,000,000 | Platform development and IP creation. |
| **Marketing** | **15%** | 1,800,000,000 | Global partnerships and brand awareness. |
| **Team** | **10%** | 1,200,000,000 | Core contributors (Subject to vesting). |
| **Reserve** | **10%** | 1,200,000,000 | Emergency funds and liquidity provision. |
| **Public/Private Sale** | **5%** | 600,000,000 | Initial fundraising. |
""",

    "roadmap/roadmap.md": """# Development Plan

Our journey is divided into 4 phases, symbolizing the cycle of time and growth.

![Roadmap Timeline Placeholder](Placeholders/roadmap_timeline.png)

## Phase 1: The Beginning (Q1 - Q2)
> *Setting the Foundation*

* ✅ **Concept Design:** Finalizing the 12 Zodiac characters.
* ✅ **Whitepaper V1.0:** Release of technical and cultural documentation.

## Phase 2: Expansion (Q3 - Q4)
> *Building the Ecosystem*

* **Token Generation Event (TGE):** Official launch of 12C token.
* **NFT Collection:** First genesis drop of 12 Zodiac NFTs.

## Phase 3: Circulation (Next Year Q1-Q2)
> *Utility & Rewards*

* **Mini-Game Launch:** "12cycle Run" (Beta).
* **Staking Service:** Proof of Culture staking open.

## Phase 4: The Universe (Future)
> *Global Standard*

* **12cycle DAO:** Governance transition to the community.
* **Metaverse Integration:** Full 3D world opening.
"""
}

def create_whitepaper_structure():
    # 현재 위치 확인
    base_path = os.getcwd()
    print(f"Working in: {base_path}")

    for file_path, content in files.items():
        # 전체 경로 생성
        full_path = os.path.join(base_path, file_path)
        directory = os.path.dirname(full_path)

        # 폴더가 없으면 생성 (ecosystem, tokenomics, roadmap 등)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")

        # 파일 쓰기
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Created file: {file_path}")

    # 이미지 플레이스홀더 폴더 생성
    placeholder_dir = os.path.join(base_path, "Placeholders")
    if not os.path.exists(placeholder_dir):
        os.makedirs(placeholder_dir)
        print("Created directory: Placeholders")

if __name__ == "__main__":
    create_whitepaper_structure()
    print("\n✅ All files generated successfully!")