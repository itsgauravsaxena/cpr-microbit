# Uge 8 — Heartbeat Beacon (radio, del 2 af 2)

💗 Én micro:bit gemmer sig og hvisker *hej* på radioen; den anden leder efter den — og bliver **varmere**, jo tættere den kommer. En skattejagt med lys!

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="et pulserende radiofyr" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<g fill="#2b3038"><rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g>
<g fill="#ff4d4d"><g><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="1;0;0"/><rect x="85" y="85" width="26" height="26" rx="6"/></g><g><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;1;0"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/></g><g><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;0;1"/><rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g></g>
</svg>
</div>

**Mål:** byg videre på sidste uges radiogrundlag — én micro:bit udsender et lavenergi-"hej" på en radiokanal, den anden registrerer det og viser et hjerte, når den er tæt på. Lav det derefter om til et gemme-beacon-jagtspil.

**Officiel tutorial:** https://microbit.org/projects/make-it-code-it/heartbeat-beacon/

**Fortsætter fra:** [Uge 7 — Micro Chat](../week-07-micro-chat/README.md).

## Sessionsforløb (60 min)
- 5 min opsummering af radiogrundlaget fra uge 7
- 35 min — Heartbeat Beacon-tutorial: én micro:bit udsender et lavenergi-"hej" på en radiokanal, den anden registrerer det og viser et hjerte, når den er tæt på
- 15 min — lav det om til et spil: gem sender-micro:bitten et sted i lokalet, børnene bruger modtageren til at "jage" den (det bliver varmere, når signalet bliver stærkere)
- 5 min — afrunding

## Noter
_(plads til sessionsnoter)_

## Reference
- Radiogrupper er som walkie-talkie-kanaler — samme kanalnummer = samme samtale, indstilles i `on start`
